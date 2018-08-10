from operator import add

import numpy as np
import requests

import matplotlib.pyplot as plt
from fpdf import FPDF


def get_my_review(my_ids: dict) -> dict:
    # get github information
    github_id = my_ids['github']
    github_info = get_github_info(github_id)
    save_result(github_info['commit_by_weeks'])
    return github_info


def get_github_info(git_id: int) -> dict:
    github_info = {}
    git_user_info = requests.get('https://api.github.com/users/{}'.format(git_id))

    if git_user_info.status_code == 200:
        git_user_info_json = git_user_info.json()
        github_info = {
            'nb_repos': git_user_info_json['public_repos'],
            'commit_by_weeks': [0] * 52
        }
        git_list_repos = requests.get('https://api.github.com/users/{}/repos'.format(git_id))

        if git_list_repos.status_code == 200:
            git_list_repos_json = git_list_repos.json()
            for repo in git_list_repos_json:
                git_nb_commit_by_week = requests.get(
                    'https://api.github.com/repos/{}/{}/stats/participation'.format(
                        git_id, repo["name"]
                    )
                )

                if git_nb_commit_by_week.status_code == 200:
                    git_nb_commit_by_week_json = git_nb_commit_by_week.json()
                    if git_nb_commit_by_week_json.get('owner'):
                        github_info['commit_by_weeks'] = list(
                            map(add, github_info['commit_by_weeks'],
                                git_nb_commit_by_week_json['owner']
                                )
                        )
    return github_info


def save_result(nb_commits_by_weeks: list) -> bool:
    weeks = [x for x in range(1, len(nb_commits_by_weeks) + 1)]
    plt.plot(np.arange(1, len(nb_commits_by_weeks) + 1), nb_commits_by_weeks)
    plt.ylabel('nb of commits')
    plt.xlabel('week')
    plt.xticks(weeks)
    plt.title('Github activity')
    plt.savefig('diane_delallee_github_activity.png')

    images = ['diane_delallee_github_activity.png']
    pdf = FPDF()
    for image in images:
        pdf.add_page()
        pdf.image(image, -2, 15)
    pdf.output("diane_delallee_report.pdf", "F")


if __name__ == "__main__":
    my_ids = {
        'github': 'dianedelallee',
        'stackoverflow': 4640061
    }

    statistics = get_my_review(my_ids)
