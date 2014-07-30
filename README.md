django-base-template
====================

A modern django (1.6) template for new projects.



Authors
=======

- Manuel García / [@mgdo85 at twitter](https://www.twitter.com/mgdo85) / [linkedin](http://es.linkedin.com/in/mgdo85/) 
- Ramón García / [@rmngrc at twitter](https://www.twitter.com/rmngrc) / [linkedin](http://es.linkedin.com/in/rmngrc/) 


Feel free to contact us for feedback or contributions. This project is still in hard development.



Getting Started
===============

If you are an experienced django developer, probably you can skip this step, but if you are new in django you need to configure your environment to start using this template. For Mac users:

- Install Homebrew, Python 2.7 and some dependencies:

```
$ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
$ brew install python
$ brew install pillow
$ pip install virtualenvwrapper
```

- Then, add the lines at the end of your ``.profile`` file:

```
$ echo "PATH=/usr/local/bin:/usr/local/share/python:\$PATH" >> ~/.profile
$ echo "export PATH" >> ~/.profile
$ echo "export WORKON_HOME=\$HOME/.virtualenvs" >> ~/.profile
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
$ echo "export PIP_VIRTUALENV_BASE=\$WORKON_HOME" >> ~/.profile
```

- Reload your ``.profile`` settings:

```
$ source .profile
```

- Configure your virtual environment:

```
$ mkdir -p ~/Sites/<project_name>
$ mkvirtualenv -a ~/Sites/<project_name> <project_name>
```

- And finally, install django in this virtual environment. Don't forget to use ``workon <project_name>`` if your are not currently working with the ``<project_name>``virtual env.

```
$ pip install django
```



Download Project
================

As simple as (remember, ``workon <project_name>`` if not activated):

```
$ django-admin.py startproject --template=https://github.com/mgdo85/django-base-template/archive/master.zip --extension=py,rst,rb,html,gitignore <project_name> .
$ pip install -r requirements/development.txt
```



Next Steps
===========

Coming soon. 