from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

from django.views.generic import DetailView, ListView, CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Group

from app.main_screen.forms import PollCreateForm
from app.main_screen.models import ListNewsModel, PollInfoModel, CustomUserModel, TopicNameModel

# Create your views here.

class HomeScreenView(PermissionRequiredMixin, ListView):
    model = ListNewsModel
    permission_required = 'main_screen.view_listnewsmodel'
    context_object_name = 'news_list'  

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
        my_dicters = {}
        for index, value in enumerate(self.request.POST.getlist('additional_input', '')):
            my_dicters[f'{index}. {value}'] = 0
        form.instance.json_variants = my_dicters
        return super().form_valid(form)

class IntermediateListView(PermissionRequiredMixin, ListView):
    model = TopicNameModel
    permission_required = 'main_screen.view_topicnamemodel'
    

class CheckPollView(PermissionRequiredMixin, ListView):
    permission_required = 'main_screen.view_pollinfomodel'
    model = PollInfoModel

    def get_queryset(self):
        index_theam = self.kwargs.get('id_theam')
        query = self.model.objects.exclude(pk__in=self.request.user.custom_user.poll_status.all()).filter(topic=TopicNameModel.objects.get(pk=index_theam), status=True)
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_poll'] = self.get_queryset().first() 
        print(context['first_poll'])
        return context

    def post(self, request, *args, **kwargs):
        variants = request.POST.getlist('variant')
        first_poll = self.get_queryset().first()
        users = request.user.custom_user
        if not first_poll:
            return redirect(reverse('list_poll', kwargs={'id_theam': self.kwargs.get('id_theam')}))
        
        users.poll_status.add(first_poll)
        # В дальнейшем переделаем логику 
        users.money += 10000 / first_poll.max_vote
        json_sp = first_poll.json_variants

        for variant in variants:
            json_sp[variant] += 1

        if sum(json_sp.values()) >= first_poll.max_vote:
            first_poll.status = False
            
        first_poll.json_variants = json_sp
        first_poll.vote +=  1
        first_poll.save()
        users.save()
        
        return redirect(reverse('list_poll', kwargs={'id_theam': self.kwargs.get('id_theam')}))


class CheckProfile(PermissionRequiredMixin, TemplateView):
    template_name = 'main_screen/detail.html' 
    model = CustomUserModel
    permission_required = 'main_screen.view_pollinfomodel'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user  # получаем текущего пользователя
        profile = user.custom_user  # получаем профиль через related_name
        
        context['user_info'] = user
        context['profile'] = profile  # добавляем профиль в контекст
        print(profile)

        return context


class PollDetail(PermissionRequiredMixin, DetailView):
    model = PollInfoModel
    permission_required = 'main_screen.view_pollinfomodel'

