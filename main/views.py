from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.core.serializers import serialize


from main.models import Vacancy, Message, Response, Resume
from main.forms import MessageCreateForm


class VacancyListView(ListView):
    template_name = 'main/index.html'
    context_object_name = 'vacancies'
    model = Vacancy

    def get_queryset(self):
        '''возвращает список элементов queryset'''
        queryset = super().get_queryset()
        queryset = queryset.filter(is_public=True)
        return queryset
   


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
def vacancy_date_update_view(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if not request.user == vacancy.author:
        return HttpResponseForbidden()
    vacancy.save()
    return redirect('account_detail', vacancy.author.username)

def get_messages_view(request, pk):
    response = get_object_or_404(Response, pk=pk)
    context = {}
    context['message_create_form'] = MessageCreateForm()
    context['response'] = response
    return render(request=request, template_name='main/modal_message_partial.html', context=context)


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
        return reverse('account_detail', kwargs={'slug': self.request.user.username})

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


class ResponseCreateView(CreateView):
    model = Response

    def post(self, request, *args, **kwargs):
        vacansy_pk = kwargs.get('pk')
        vacancy = get_object_or_404(Vacancy, pk=vacansy_pk)
        applicant = request.user
        resume_pk = request.POST.get('resume_pk')
        resume = get_object_or_404(Resume, pk=resume_pk)
        response = Response.objects.create(vacancy=vacancy, applicant=applicant, resume=resume)
        
        message_text = request.POST.get('message_text')
        Message.objects.create(response=response, author=applicant, text=message_text)


 
        return redirect('vacancy_detail', pk=vacansy_pk)
    
