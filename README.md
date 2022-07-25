# alien-project

Alien game, unfinished.

### Requirements

To run you will need: [NodeJS](https://nodejs.org/) and [Poetry](https://python-poetry.org/)

### To run:

```
git clone https://github.com/SoMir0/alien-project.git
cd alien-project/frontend
npm ci
npm run build
cd ..
poetry install
DJANGO_DEBUG=ON poetry run python manage.py makemigrations
DJANGO_DEBUG=ON poetry run python manage.py migrate
DJANGO_DEBUG=ON poetry run python manage.py runserver
```
