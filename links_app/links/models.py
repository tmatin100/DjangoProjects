from django.db import models

# Create your models here.
# save a shortened link - name, url , slug, # of clicks
class Link(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    url = models.URLField(max_length=200)
    # mysite.com/link/q
    # mysite.com/link/name-of-link
    slug = models.SlugField(unique=True, blank=True)
    clicks = models.PositiveIntegerField(default=0)

    def __str__()


    
    