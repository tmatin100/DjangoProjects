from typing import List
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django import forms

from .models import Trip, Note



# Create your views here.

    # class based view 
class HomeView(TemplateView):
    template_name = 'trip/index.html'

    # function based view 
@login_required
def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)
    # creates a context variable so we can pass it in to our render function 
    context = {
        'trips': trips
    }
    return render(request, 'trip/trip_list.html', context)

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']
    # template name  model_form.html

    def form_valid(self, form):
        # owner field = logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)

class TripDetailView(DetailView):
    model = Trip 
# data stored on Trip - also have the Notes data  def clean_FIELD(self):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes
        return context

class TripUpdateView(UpdateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ["city", "country", "start_date", "end_date"]
    #template named model_form.html

class TripDeleteView(DeleteView):
    model = Trip
    success_url = reverse_lazy('trip-list')




class NoteDetailView(DetailView):
    model = Note 


class NoteListView(ListView):
    model = Note
    def get_queryset(self):  #using metod ovveride to get the queryset of a user 
        queryset = Note.objects.filter(trip__owener=self.request.user)
        return queryset


class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"
    # overide the get_form method to get data only for the logged user
    def get_form(self):    
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)  # gets the trips but filter by logged in user 
        form.fields['trip'].queryset = trips  # since its a foreign key relationship, we are modyfying this for just the trips for the logged i user
        return form

class NoteUpdateView(UpdateView):
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"

    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        form.fields['trip'].queryset = trips
        return form
    
class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')
    #not make the template - send post requests here

