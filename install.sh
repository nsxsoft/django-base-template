#!/bin/sh

# Ask user for ROOT password one single time
echo -n Password:
read -s password

# Install django dependencies
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
brew install python
brew install pillow
pip install virtualenvwrapper

# Update .profile
if [[ "$PATH" == */usr/local/bin*  || "$PATH" == */usr/local/share/python* ]]
then
    echo "PATH=/usr/local/bin:\$PATH" >> ~/.profile
    echo "PATH=/usr/local/share/python:\$PATH" >> ~/.profile
    echo "export PATH" >> ~/.profile
fi

if [[ -z "$WORKON_HOME" ]]
then
    echo "export WORKON_HOME=\$HOME/.virtualenvs" >> ~/.profile
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
    echo "export PIP_VIRTUALENV_BASE=\$WORKON_HOME" >> ~/.profile
fi

# Reload .profile after changes
source ~/.profile

# Create project virtualenv
mkdir -p ~/Sites/{{ project_name|lower }}
mkvirtualenv -a ~/Sites/{{ project_name|lower }} {{ project_name|lower }}

# Install dependencies for development
pip install -r requirements/development.txt