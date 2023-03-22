# Starter project
## Run project 

You need to have installed [python](https://www.python.org/) and [virtualenv](https://pypi.org/project/virtualenv/) in your SO

``` bash
# VENV
$ virtualenv .venv
$ source .venv/Scripts/activate         # (Windows Bash)

$ source .venv/bin/activate             # (macOS or Linux)
$ .venv/Scripts/activate                # (Windows PowerShells)  
-----------
# INSTALL
$ pip install Django                    
$ pip install -r requirements.txt
-----------
# INIT 
$ django-admin startproject conf .
$ python manage.py startapp recetas  
# [1] Ajustes urls 
# [2] INSTALLED_APPS
-----------
# RUN
$ python manage.py runserver 8000     # Start
-----------
# MIGRATIONS
$ python manage.py makemigrations 
$ python manage.py migrate
```

[1] Ajustes Urls

recetas/urls.py
```
from django.urls import path

from . import views

app_name = "recetas"
urlpatterns = [
    path('', views.index, name='index'),
]
```

conf/urls.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recetas.urls', namespace='recetas'))
]
```

[2] Añadir 'recetas' a INSTALLED_APPS

conf/settings.py
```
INSTALLED_APPS = [
    ...
    'recetas',
]
```

[3] Variables de entorno 

Instalar [python-dotenv](https://pypi.org/project/python-dotenv/)
```
pip install python-dotenv
```

Crear fichero `.env` con las variables
```
DEBUG=1
DJANGO_SECRET_KEY='change_me'
...
```
En `settings.py`
```
from dotenv import load_dotenv
import os 

load_dotenv()

...
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')
DEBUG = int(os.environ.get('DEBUG', default=0))
...
```