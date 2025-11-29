# EnterpriseAPI

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![Django 5](https://img.shields.io/badge/django-5.0%2B-brightgreen)](https://www.djangoproject.com/)
[![JWT](https://img.shields.io/badge/auth-JWT-success)](https://jwt.io/)
[![Poetry](https://img.shields.io/badge/deps-poetry-7f00ff)](https://python-poetry.org/)

Modern Django 5 + DRF API with JWT authentication, modular apps and OpenAPI schema.

## Features
- JWT auth via djangorestframework-simplejwt
- Custom user model + refresh tokens
- Three clean apps: `authenticate`, `companies`, `storages`
- OpenAPI 3 schema via drf-spectacular
- Permission classes per app
- Ready for async, Celery, Redis (structure prepared)

## Stack
- Django 5 · DRF · simplejwt · drf-spectacular
- Poetry for dependency management
- PostgreSQL-ready

## Run
```bash
git clone https://github.com/perilka/EnterpriseAPI.git
cd EnterpriseAPI

# With Poetry
poetry install
poetry shell
cd app
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Structure
```text
app/
├── authenticate/    # custom user + JWT views
├── companies/       # company CRUD + permissions
├── storages/        # file/document storage logic
└── core/            # settings, urls
```

---

*Developed by 🐳 perilka 🐳 to to demonstrate modern Django 5 + JWT backend patterns used in commercial projects. Explore my resume and another repositories for similar production work!!!*
