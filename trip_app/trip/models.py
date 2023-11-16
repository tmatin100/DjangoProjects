from django.db import models
from django.contrib.auth import get_user_model # defualt django out of the box user model 
from django.core.validators import MaxValueValidator
# Create your models here.
# trips & notes tables (stores images)

# we can use the user model like this to get user
User = get_user_model()

class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    start_date = models.DateField(blank=True, null=True)  # blank and null true means this is not a required field
    end_date = models.DateField(blank=True, null=True)  
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')  # we can pass in the foreign key relationship to the user model 
                                             # allows only logged in users to see their trips 
                                             # on delete deltes all of the table assoiated with the user when a user gets deleted
                                            # we can use the trips from the user model 

    def __str__(self):
        return self.city   # returns the string representaion of a trip object instance ex. city


class Note(models.Model):
    # Predefined choices to select from in the type field 
    EXCURSIONS = (
        ("event", "Event"),
        ("dining", "Dining"),
        ("experience", "Experience"),
        ("general", "General"),
    )

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=100)
    description = models.TextField()   # unlike a character field it has no limits 
    type = models.CharField(max_length=100, choices=EXCURSIONS) # will let user select this from a predefined list , in this case EXCURSIONS which is a tupple of tupples 
    img = models.ImageField(upload_to='notes', blank=True, null=True)
    # needs the pillow packagee: pip install pillow
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)])

    def __str__(self):
        return f'{self.name} in {self.trip.city}'