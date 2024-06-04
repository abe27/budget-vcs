"""
Django settings for webbase project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*^m1rudl5tihf^igm$fbzxf=6r_jegbb)(fnod&9t3d#&exw1@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["https://edi-vcst.in.th","edi-vcst.in.th","https://budget.edi-vcst.in.th","budget.edi-vcst.in.th","125.25.57.91", ]
CSRF_TRUSTED_ORIGINS = ["https://edi-vcst.in.th"]
if DEBUG:
    ALLOWED_HOSTS = ["*"]
    # CSRF_TRUSTED_ORIGINS = ["*"]

# Application definition

INSTALLED_APPS = [
    # 'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'budgetapp.apps.BudgetappConfig',
    'budgetaaa.apps.BudgetaaaConfig',
    'budgetbvs.apps.BudgetbvsConfig',
    'formulavcst.apps.FormulavcstConfig',
    'inventoryapp.apps.InventoryappConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webbase.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        "DIRS": [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'webbase.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    "budget_vcst": {
        "ENGINE": "mssql",
        "NAME": "Store_INVENTORY",
        "USER": "fm1234",
        "PASSWORD": "x2y2",
        "HOST": "192.168.20.9",
        "PORT": "1433",
        "Trusted_Connection": "no",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",},
    },
    "formula_vcst": {
        "ENGINE": "mssql",
        "NAME": "formula",
        "USER": "fm1234",
        "PASSWORD": "x2y2",
        "HOST": "192.168.20.9",
        "PORT": "1433",
        "Trusted_Connection": "no",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",},
    },
      "budget_vcs": {
        "ENGINE": "mssql",
        "NAME": "BUDGET",
        "USER": "fm1234",
        "PASSWORD": "x2y2",
        "HOST": "192.168.5.12",
        "PORT": "1433",
        "Trusted_Connection": "no",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",},
    },
    "formula_vcs": {
        "ENGINE": "mssql",
        "NAME": "formula",
        "USER": "fm1234",
        "PASSWORD": "x2y2",
        "HOST": "192.168.5.12",
        "PORT": "1433",
        "Trusted_Connection": "no",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",},
    },
    "budget_aaa": {
        "ENGINE": "mssql",
        "NAME": "BUDGET",
        "USER": "fm1234",
        "PASSWORD": "x2y2",
        "HOST": "192.168.10.6",
        "PORT": "1433",
        "Trusted_Connection": "no",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",},
    },
    "formula_aaa": {
        "ENGINE": "mssql",
        "NAME": "formula",
        "USER": "fm1234",
        "PASSWORD": "x2y2",
        "HOST": "192.168.10.6",
        "PORT": "1433",
        "Trusted_Connection": "no",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",},
    },
    "budget_bvs": {
        "ENGINE": "mssql",
        "NAME": "BUDGET",
        "USER": "fm1234",
        "PASSWORD": "x2y2",
        "HOST": "192.168.1.191",
        "PORT": "1433",
        "Trusted_Connection": "no",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",},
    },
    "formula_bvs": {
        "ENGINE": "mssql",
        "NAME": "formula",
        "USER": "fm1234",
        "PASSWORD": "x2y2",
        "HOST": "192.168.1.191",
        "PORT": "1433",
        "Trusted_Connection": "no",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server",},
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATABASE_ROUTERS = ["webbase.db.DBBudgetRouter"]
