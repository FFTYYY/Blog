"""
Django settings for YYYBlog project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from .setting_secret_key import SECRET_KEY

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# SECURE_SSL_REDIRECT = True

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django_extensions',
	'Entry.apps.EntryConfig',
	'Article_Zone.apps.ArticleZoneConfig',
	'Open_Discuss_Zone.apps.OpenDiscussZoneConfig',
	'Free_Page_Zone.apps.FreePageZoneConfig',
	'Universe.apps.UniverseConfig',
	"ckeditor" ,
	'ckeditor_uploader',
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

ROOT_URLCONF = 'YYYBlog.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'YYYBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

CKEDITOR_UPLOAD_PATH = 'uploads'
CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
	"default" : {
		"language" : "zh-cn" ,
		"width" : "1000px" ,
		"height" : "400px" ,
		"tabSpaces" : 8 ,
		"disableObjectResizing" : False , 
		'toolbar': 'Custom',
		'toolbar_Custom': [
            ['Bold','Italic','Underline','Strike','-','Subscript','Superscript'], 
            ['Styles','Format','Font','FontSize'], 
			['div','Source','-','Save','NewPage','Preview','-','Templates'], 
            ['Cut','Copy','Paste','PasteText','PasteFromWord'], 
            ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'], 
            ['TextColor','BGColor'], 
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'], 
            ['Link','Unlink','Anchor'], 
            ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'], 
            ['Maximize','ShowBlocks',],
            ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'], 
            ["YYYSpliter" , "YYYRegulizeSpliter"] , 
            
            ['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'], 
		],
		'enterMode' : 2,
		'removePlugins': 'stylesheetparser',
		"allowedContent" : True , 
		"disallowedContent" : True, 		
	},
}