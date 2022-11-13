from django.shortcuts import render
from django.views.generic import ListView, CreateView

from main.models import Vacancy
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
        