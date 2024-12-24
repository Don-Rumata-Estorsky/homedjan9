"""
Django settings for Pilgrim project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent         
#в дасе_дир этот файл и функция абсолютного пути  . его парент пилгрим а егоо пайтон 



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u%d&!f&#8b)&bdw642q5h3raro4@vzm_f&t_ml6jwct0&*&i@_'
# зайти на сайт джанго сикрет кеи и взять код получьше  
#     ... у нас есть база дайных 


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] 


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin', #страеица админа панель 
    'django.contrib.auth', #заход выход и аунттификация
    'django.contrib.contenttypes', # отображения 
    'django.contrib.sessions', # сесии 
    'django.contrib.messages', #эвеннт сообщение
    'django.contrib.staticfiles', #стиль статистие файлы
    'app'
]

MIDDLEWARE = [ #слои вхождения и выхождения в тетради есть 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Pilgrim.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [ # есть на сайте 4 страницы нужно отображжать число пользователей и что бы не делать отдельные
                # функции можно закинуть сюда по умолчаию 
                'django.template.context_processors.debug',
                
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Pilgrim.wsgi.application'
# ддля запуска в сети инет

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# база 
#
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',# чтобы пароль не совпадал с названиями
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', #мин количество символов
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',#обычность паролья
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',#12345 с рифмой с детства я дружу
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us' #можно сменть язык

TIME_ZONE = 'UTC'#встроиные утилиты ! важно знать 

USE_I18N = True#переводить язык

USE_TZ = True#таймзоны


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'#ЛОГИ журнал проишествий 

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'