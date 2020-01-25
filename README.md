# [Digiskills](https://digiskills.kg)
Digiskills - platform designed for develop technical skills and competence of our citizens. 
Project was powered by 
[State Committee on Information Technologies and Communications of the Kyrgyz Republic](https://digital.gov.kg) 
and by [Neobis clubs](https://neobis.kg).


## Developer guide
In this repository you can find only Back-End & Dev-Ops source code. 
Front was included [here](https://github.com/Aidanaaidlanova/digitalskills). 
So you can find in docker-compose.yml docker build front from git source. 
API documentation you can find in ```apiary.apib``` 
and [here](https://digiskills2.docs.apiary.io/#)

Used for Back-End:
* Python
* Django & Django Rest Framework.

## Setup Back-End
* Put .env to src/ by .env.Example (make sure you use DEBUG=True for local)
* ```docker-compose up back```
* ```docker-compose run --rm back /bin/bash -c "cd src; ./manage.py migrate"```

or 
* Put .env to src/ by .env.Example (make sure you use DEBUG=True for local)
* ```python -m venv .venv```
* ```source .venv/bin/activate```
* ```pip install -r requirenments.txt```
* ```cd src```
* ```python manage.py migrate```
* ```python manage.py runserver```

## Run tests
* ```cd src```
* ```python3 manage.py test```

## Deployment
* Put .env to src/ by .env.Example (make sure you use DEBUG=False for prod)
* ```sudo docker-compose -f docker-compose.yml -f docker-compose-first-prod.yml up ```
* ```sudo docker-compose -f docker-compose.yml -f docker-compose-first-prod.yml down ```
* And again```sudo docker-compose -f docker-compose.yml -f docker-compose-prod.yml up -d```
* Then add ssl_renew.sh to cron jobs.

I followed for [this](http://pawamoy.github.io/2018/02/01/docker-compose-django-postgres-nginx.html) 
and [this](https://www.digitalocean.com/community/tutorials/how-to-secure-a-containerized-node-js-application-with-nginx-let-s-encrypt-and-docker-compose)
tutorials to dockerize this project.
So good luck! Pray to get no issues!

