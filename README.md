## Setup project
* create virtualenv and activate
* pip3 install -r requirenments.txt
* python3 manage.py migrate
* python3 manage.py collecstatic
* python3 manage.py runserver
* celery worker --app digiskills.celery --loglevel=debug