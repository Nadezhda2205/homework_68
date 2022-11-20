from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin


from main.models import Vacancy, Message, Response
from main.forms import MessageCreateForm
# from accounts.models import Account


class VacancyListView(ListView):
    template_name = 'main/index.html'
    context_object_name = 'vacancies'
    model = Vacancy

    def get_queryset(self):
        '''возвращает список элементов queryset'''
        queryset = super().get_queryset()
        queryset = queryset.filter(is_public=True)
        return queryset
    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if not self.request.user.is_authenticated:
    #         return context
    #     user: Account

class VacancyCreateView(CreateView):
    template_name = 'main/create_vacancy.html'
    model = Vacancy
    fields = [
        'name', 
        'salary', 
        'description', 
        'experience_time',
        'vacancy_category',
        'is_public'
        ]
    success_url = '/'

    def form_valid(self, form):
        self.object: Vacancy = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)

class VacancyDetailView(DetailView):
    template_name = 'main/detail_vacancy.html'
    model = Vacancy
    context_object_name = 'vacancy'

    
class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'main/update_vacancy.html'
    model = Vacancy
    fields = [
        'name', 
        'salary', 
        'description', 
        'experience_time',
        'vacancy_category',
        'is_public'
        ]
    context_object_name = 'vacancy'
    
    def get_success_url(self):
        return reverse('vacancy_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().author == request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


@login_required
def VacancyDateUpdateView(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if not request.user == vacancy.author:
        return HttpResponseForbidden()
    vacancy.save()
    return redirect('account_detail', vacancy.author.username)
    

class ResponseDetailView(LoginRequiredMixin, DetailView):
    template_name = 'main/detail_response.html'
    model = Response
    context_object_name = 'response'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = MessageCreateForm()
        context['form'] = form
        return context

    def dispatch(self, request, *args, **kwargs):
        '''
        pk отклика
        конкретный отклик по pk
        автор отклика(откликнувшийся)
        автор вакансии
        условие если юзер == откликнувшемуся или юзер == автору вакансии,
        то разрешаем просмотр отклика
        '''
        response_pk = self.kwargs.get('pk')
        response: Response = get_object_or_404(Response, pk=response_pk)
        applicant_response = response.applicant
        author_vacancy = response.vacancy.author
        if request.user == applicant_response or request.user == author_vacancy:
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm

    def form_valid(self, form):
        self.object: Message = form.save(commit=False)
        response_pk = self.kwargs.get('pk')
        self.object.response = get_object_or_404(Response, pk=response_pk)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('response_detail', kwargs={'pk': self.kwargs.get('pk')})

    def dispatch(self, request, *args, **kwargs):
        '''
        pk отклика
        конкретный отклик по pk
        автор отклика(откликнувшийся)
        автор вакансии
        условие если юзер == откликнувшемуся или юзер == автору вакансии,
        то разрешаем добавить сообщение
        '''
        response_pk = self.kwargs.get('pk')
        response: Response = get_object_or_404(Response, pk=response_pk)
        applicant_response = response.applicant
        author_vacancy = response.vacancy.author
        if request.user == applicant_response or request.user == author_vacancy:
            return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()
