from django.apps import AppConfig
from django.http import request
from views import home


class MongodbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mongodb'

