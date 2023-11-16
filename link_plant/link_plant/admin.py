from django.contrib import admin

# import your models Pofile and Link 

from .models import Profile, Link

# Register your models here.
admin.site.register(Profile)
admin.site.register(Link)


#  python manage.py createsuperuser
#tmatin
#dom@sup.com
#Admin123