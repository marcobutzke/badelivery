from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-p@tqa*bcllz4t+siya9g4_dwh*-5)0s7!et0_njw(%lspsfmto'
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'administrativo',
    'allauth_ui',
    'allauth',
    'allauth.account',
    'widget_tweaks',
    'slippers',
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'producao.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'producao.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'delivery',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'postgres',
#        'USER': 'postgres.imewrseyfhbxprzvxwrt',
#        'PASSWORD': 'Innverness#30',
#        'HOST': 'aws-0-us-west-2.pooler.supabase.com',
#        'PORT': '6543',
#    }
#}


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

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = "none"
ALLAUTH_UI_THEME = 'silk'

SIMPLEUI_DEFAULT_THEME = 'orange.css'
SIMPLEUI_CONFIG = {
    'system_name': 'Biano Alimentos',
    'menus': [
        {
            'name': 'Operações',
            'icon': 'fas fa-boxes-packing',
            'models': [
                {'name': 'Periodo', 'url': 'administrativo/periodo/', 'icon': 'fas fa-calendar'},
                {'name': 'Compra', 'url': 'administrativo/compra/', 'icon': 'fas fa-briefcase'},
                {'name': 'Producao Diária', 'url': 'administrativo/producao/', 'icon': 'fas fa-industry'},
                {'name': 'Manufatura Diária', 'url': 'administrativo/manufatura/', 'icon': 'fas fa-building'},
                {'name': 'Pedido', 'url': 'administrativo/pedido/', 'icon': 'fas fa-book'},
                {'name': 'Entrega', 'url': 'administrativo/carga/', 'icon': 'fas fa-dolly'},
                {'name': 'Contas a Pagar', 'url': 'administrativo/contaapagar/', 'icon': 'fas fa-wallet'},
                {'name': 'Contas a Receber', 'url': 'administrativo/contasareceber/', 'icon': 'fas fa-money-check'},
                {'name': 'Lançamento', 'url': 'administrativo/lancamento/', 'icon': 'fas fa-bars-progress'},
            ]
        },
        {
            'name': 'Cadastro',
            'icon': 'fas fa-box-open',
            'models': [
                {'name': 'Cliente', 'url': 'administrativo/cliente/', 'icon': 'fas fa-address-book'},
                {'name': 'Fornecedor', 'url': 'administrativo/fornecedor/', 'icon': 'fas fa-address-card'},
                {'name': 'Ingrediente', 'url': 'administrativo/ingrediente/', 'icon': 'fas fa-list-check'},
                {'name': 'Acessório', 'url': 'administrativo/acessorio/', 'icon': 'fas fa-list-check'},
                {'name': 'Produto', 'url': 'administrativo/produto/', 'icon': 'fas fa-list-check'},
            ]
        },
        {
            'name': 'Tabelas',
            'icon': 'fas fa-clipboard-check',
            'models': [
                {'name': 'Categoria', 'url': 'administrativo/categoria/', 'icon': 'fas fa-table'},
                {'name': 'Unidade', 'url': 'administrativo/unidade/', 'icon': 'fas fa-table'},
                {'name': 'Segmento', 'url': 'administrativo/segmento/', 'icon': 'fas fa-table'},
                {'name': 'Tipo', 'url': 'administrativo/tipo/', 'icon': 'fas fa-table'},
                {'name': 'Indicador', 'url': 'administrativo/indicador/', 'icon': 'fas fa-table'},
                {'name': 'Conta', 'url': 'administrativo/conta/', 'icon': 'fas fa-table-columns'},
                {'name': 'Operacao', 'url': 'administrativo/operacao/', 'icon': 'fas fa-table-columns'},
            ]
        },
        {
            'name': 'Usuários e Grupos',
            'icon': 'fas fa-user-tie',
            'models': [
                {'name': 'Usuários', 'url': 'auth/user/', 'icon': 'fas fa-user'},
                {'name': 'Grupos', 'url': 'auth/group/', 'icon': 'fas fa-users'}
            ]
        }
    ]
}