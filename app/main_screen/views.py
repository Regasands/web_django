from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm

from app.main_screen.forms import PollCreateForm
from app.main_screen.models import ListNewsModel, PollInfoModel, CustomUserModel

# Create your views here.



class HomeScreenView(ListView):
    model = ListNewsModel


class CreateUsersView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'main_screen/register.html'

    def form_valid(self, form):
        user = form.save()
        CustomUserModel.objects.create(profile=user)
        return super().form_valid(form)


class CreatePollViews(CreateView):
    form_class = PollCreateForm
    success_url = reverse_lazy('home_page')
    template_name = 'main_screen/create_poll.html'

    def form_valid(self, form):
        form.instance.user_create = self.request.user.custom_user
        return super().form_valid(form)