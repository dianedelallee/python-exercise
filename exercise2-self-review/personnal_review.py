from operator import add

import numpy as np
import requests

def get_my_review(my_ids: dict) -> dict:
    # get github information
    github_id = my_ids['github']
    github_info = get_github_info(github_id)
    save_result(github_info)
    return github_info


def get_github_info(git_id: str) -> str:
    github_info = {}
    request = 'https://github.com/{}?tab=overview&from=2018-09-01&to=2018-09-21'.format(git_id)

    git_user_info = requests.get(request, )
    git_user_info_html = ''
    if git_user_info.status_code == 200:
        git_user_info_html = git_user_info.text
        
    return git_user_info_html





def save_result(github_info: str) -> bool:
    from weasyprint import HTML
    pdf = HTML(string=github_info.encode('utf-8'))
    pdf.write_pdf('review.pdf', stylesheets=["https://assets-cdn.github.com/assets/frameworks-1ca00d32d1a8adc78ae7bb6677410eb1.css",
                                             "https://assets-cdn.github.com/assets/github-5043b3d96d50b119b971c2cdde4e0a62.css",
                                             "https://assets-cdn.github.com/assets/site-f84f81f77b3e1a4462036783c13c150d.css"])   
    print('pdf printed')
    return True


if __name__ == "__main__":
    my_ids = {
        'github': 'dianedelallee',
        'stackoverflow': 4640061
    }

    statistics = get_my_review(my_ids)
