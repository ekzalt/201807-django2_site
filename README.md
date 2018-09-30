# 201807-django2_site

Python Web Frameworks:
- Django,
- Flask,
- Web2Py,
- CherryPy,
- Pyramid,
- Tornado,
- TurboGears

Django, Flask имеют следующие соглашения:
- html шаблоны хранятся в папке: templates
- статические файлы для отдачи хранятся в папке: static

Django Framework
https://www.djangoproject.com/

```bash

# install django
pip install Django==2.1.1

# check django version
python -m django --version
django-admin --version

# create new project with name 'mysite'
django-admin startproject mysite

# run dev server at http://127.0.0.1:8000/
python manage.py runserver

# довавить новый раздел сайта
python manage.py startapp new_app

# выполнить стандартный список миграций с созданием БД (SQlite)
python manage.py migrate

# зарегистрировать кастомные миграции, чтобы затем выполнить их - migrate
python manage.py makemigrations

# создать админа
python manage.py createsuperuser

```
