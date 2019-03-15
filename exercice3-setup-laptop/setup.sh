#!/usr/bin/env bash

# generate ssh key
#echo "Generating an SSH key"
#ssh-keygen -t rsa -b 4096

# Install homebrew if we don't have it
if test ! $(which brew); then
  echo "Installing homebrew"
  ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi


# Install Caskroom
brew install caskroom/cask/brew-cask

# Update homebrew recipes
echo "Updating homebrew"
brew update

echo "Installing Git"
brew install git

# Install homebrew packages 

packages=(
    ansiweather
    ack
    archey
    bash-completion
    battery
    cowsay
    fortune
    git
    howdoi
    newsboat
    openssl
    pipenv
    spark
    mas
    terminal-notifier
    vegeta
    youtube-dl
    zsh
    zsh-completions
    node
    npm
    python3
    graphviz
    htop
    httpie
)

echo "Installing brew stuff..."
brew install ${packages[@]}



echo "Installing Mac App Store "
mas signin diane.delallee@gmail.com

mas install 966085870  # TickTick


echo "Cleaning up brew"
brew cleanup

echo "Installing homebrew cask"
brew install caskroom/cask/brew-cask



# Install brew Casks
apps=(
    alfred
    filezilla
    firefox
    google-chrome
    iterm2
    cheatsheet
    colorpicker
    gifox
    gimp
    brackets
    libreoffice
    jupyter-notebook-ql
    numi
    spectacle
    docker
    flux
    brackets
    franz
    gitkraken
    pycharm
    spark
    postman
    dashlane
)

# Install apps to /Applications
# Default is: /Users/$user/Applications
echo "installing apps with Cask..."
brew cask install --appdir="/Applications" ${apps[@]}

brew cask alfred link

brew cleanup


# python
easy_install pip


# Install npm
curl http://npmjs.org/install.sh | clean=no sh
# Build the index since it takes a while
npm search asdf


mkdir $HOME/workspace

# Dotfiles
#cd $HOME/workspace
#git clone https://github.com/dianedelallee/dotfiles.git
#cd dotfiles
#sh install.sh


echo "Done!"