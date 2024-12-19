from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Group

from app.main_screen.forms import PollCreateForm
from app.main_screen.models import ListNewsModel, PollInfoModel, CustomUserModel

# Create your views here.



class HomeScreenView(PermissionRequiredMixin, ListView):
    model = ListNewsModel
    permission_required = 'main_screen.view_listnewsmodel'


class CreateUsersView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'main_screen/register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_page')
        return super().get(request, *args, **kwargs)
        


    
    def form_valid(self, form):
        user = form.save()
        CustomUserModel.objects.create(profile=user)
        group = Group.objects.get(name='User')
        if group:
            group.user_set.add(user)
        return super().form_valid(form)


class CreatePollViews(PermissionRequiredMixin, CreateView):
    form_class = PollCreateForm
    success_url = reverse_lazy('home_page')
    template_name = 'main_screen/create_poll.html'
    permission_required = 'main_screen.add_pollinfomodel'

    def form_valid(self, form):
        form.instance.user_create = self.request.user.custom_user
        if not form.instance.json_variants:
            form.instance.json_variants = {}  # Установите значение по умолчанию для json_variants
        return super().form_valid(form)


class CheckPollView(PermissionRequiredMixin, ListView):
    permission_required = 'main_screen.view_pollinfomodel'
    model = PollInfoModel

