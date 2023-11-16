from django.contrib import admin

from .models import Trip, Note

# Register your models here. (uses the admin module)
admin.site.register(Trip)
admin.site.register(Note)

# on terminal create and make migration of the models
    # python mange.py makemigrations
    # python mange.py migrate 

# create superuser 
    # python mmange.py createsuperuser
    # Username: tmatin 
    # Email address : user@gmail.com
    # Password: python123

    