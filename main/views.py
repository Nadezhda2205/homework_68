from django.shortcuts import render
from django.views.generic import ListView

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

