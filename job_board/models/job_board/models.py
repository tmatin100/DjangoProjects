from django.db import models

# Create your models here.
# model => python classs
# model represents a table in the db 
# attrs are the fields 

# job posting table 
## tittle, description, company, salary

class JobPosting(models.Model):
    # id - by default id feild starts at 1 and autocompletes
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

    # admin portal displays job details instead of just object 1 2 3 
    def __str__(self):
        return f"{self.title} | {self.company} | Active: {self.is_active}"
    

# makemigrations
## -> creates inscurctions telling django how the db have changed 
## command:  python manage.py makemigrations

# migrate 
## -> Applies the above changes 
## command: python mange.py migrate


#CRUD Operations 
# create
# read
# update
# delet

# model manager -> objects
# JobPosting.obects.all()


# use the shell for the database 
## python manage.py shell
## JobPosting.objects.create(title="job posting 1" , description = "this is a great job", company="ABC Tech", salary = 100000)
### JobPosting.objects.create(title="Software Engineer" , description = "python django", company="Google", salary = 250000, is_active=True)
