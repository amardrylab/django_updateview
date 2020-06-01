from django.shortcuts import render
from .models import Student
from django.views.generic import ListView
from django.views.generic.edit import UpdateView

# Create your views here.

class StudentView(ListView):
    model=Student

class StudentUpdate(UpdateView):
	model=Student
	fields=['name', 'mark']
