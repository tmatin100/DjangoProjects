from django.db import models

# Create your models here.

# Class is a table in our db
# Profiles -> Links

# Create a Profile Table 
class Profile(models.Model): 
    BG_CHOICES=(
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
    )

    # name, slug, bg_color
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)

    # displays string representaion of the objects in admin 
    def __str__(self):
        return self.name

# Create a Links Table 
class Link(models.Model):
    # text, url, profile
    text = models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='links') # CASCADE deletes everything associated with a profile when deleted
                                                                   # 

    def __str__(self):
        return f"{self.text} | {self.url}"

# many to many
# one to one
# many to one 
