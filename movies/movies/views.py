from django.shortcuts import render, HttpResponse


# app/templates/app/index.html
# movies/templates/movies/index.html

# Create your views here.
def index(request):
    context = {
        'movies': ['The Truman Show','A Few Good Men','John Q.','The Matrix' ,'Inception','Pleasantville','The Island','Lord of the Rings']
    }
    return render(request,'movies/index.html', context)

def about(request):
    return render(request,'movies/about.html', {})



