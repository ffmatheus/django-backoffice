# Backoffice - IGS 🚀

# Manage departament and employees data

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/ffmatheus/django-backoffice.git
    $ cd django-backoffice
    
Activate the virtualenv for your project.

    $ python -m venv <name of env>

Access yor virtualenv

    $ <name of env>/Scripts/Activate.ps1
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then create and simply apply the migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

Get the url on terminal message: 

    Starting development server at http://127.0.0.1:8000/ (usually was that http://127.0.0.1:8000/)

To access the admin and api's, you'll need to create a user:

    $ python manage.py createsuperuser

Obs.: To make api requests by django-rest screen, need to login in admin session before.

Enjoy ! 