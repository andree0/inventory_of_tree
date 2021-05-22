# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inventory',
        'HOST': 'localhost',
        'PASSWORD': 'strongPassword100%',
        'USER': 'andrzej',
        'PORT': '5432'
    }
}
