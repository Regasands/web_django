from django.shortcuts import render
from django.views.generic import ListView


from app.main_screen.models import ListNewsModel
# Create your views here.


class HomeScreenView(ListView):
    model = ListNewsModel

# Create your views here.
