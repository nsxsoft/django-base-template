#!/bin/sh

# Install django dependencies
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
brew install python
brew install pillow
pip install virtualenvwrapper

# Rename `project_name`
mv project_name {{ project_name|lower }}

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

# Activate virtualenv and install dependencies for development
workon {{ project_name|lower }}
pip install -r requirements/development.txt
deactivate

# Add settings to virtualenv
echo "DJANGO_SETTINGS_MODULE=\"{{ project_name|lower }}.settings_development\"" >> ~/.virtualenvs/{{ project_name|lower }}/bin/postactivate
echo "export DJANGO_SETTINGS_MODULE" >> ~/.virtualenvs/{{ project_name|lower }}/bin/postactivate