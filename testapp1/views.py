from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Registration
# Create your views here.
class RegistrationCreate(CreateView):
    model=Registration
    fields=['fname','lname','city','email']
    success_url='/'