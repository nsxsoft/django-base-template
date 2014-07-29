Get started
===========

This project gives you a great base to start coding your projects in django.

First of all, you need django installed in your machine globally. Why? Well, you need django to generate every project using this base template:

    $ ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
    $ brew install python
    $ pip install django


We are going to place all our projects in the ``Sites`` folder (common place for Mac users). So, we need to:

    $ mkdir -p ~/Sites/<project_name>
    $ django-admin.py startproject --template=https://github.com/mgdo85/django-base-template/archive/master.zip --extension=py,rst,rb,html,gitignore <project_name> .


Then, the ``install.sh`` script helps you to install all the dependencies, configure your development environment, create the virtualenv for this project and finally install all the project requirements:

    $ ./install.sh


Next steps
===========

Coming soon. 


Authors
===========

- Manuel García / [@mgdo85 at twitter](https://www.twitter.com/mgdo85) / [linkedin](http://es.linkedin.com/in/mgdo85/)
- Ramón García / [@rmngrc at twitter](https://www.twitter.com/rmngrc) / [linkedin](http://es.linkedin.com/in/rmngrc/)