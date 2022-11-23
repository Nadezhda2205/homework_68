from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from main.forms import ResumeForm, EducationForm
from main.models import Resume, Education, Experience


class CreateResumeView(CreateView):
    form_class = ResumeForm
    model = Resume

    def get(self, request, *args, **kwargs):
        resume = Resume.objects.create(author=request.user)
        return redirect('edit_resume', pk=resume.pk)


class UpdateResumeView(UpdateView):
    template_name = 'main/create_resume.html'
    form_class = ResumeForm
    model = Resume
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateResumeView, self).get_context_data()
        resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        context['resume'] = resume
        if resume.vacancy_category is None and resume.salary is None:
            self.template_name = 'main/create_resume.html'
        else:
            self.template_name = 'main/edit_resume.html'
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().author == request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class ResumeDetailView(DetailView):
    template_name = 'main/resume_detail.html'
    model = Resume
    context_object_name = 'resume'


class ResumesIndexView(ListView):
    template_name = 'accounts/detail_applicant.html'
    model = Resume
    context_object_name = 'resumes'


class ResumeListView(ListView):
    template_name = 'main/resume_list.html'
    model = Resume
    context_object_name = 'resumes'

    def get_queryset(self):
        '''возвращает список элементов queryset'''
        queryset = super().get_queryset()
        queryset = queryset.filter(is_public=True)
        return queryset


class ResumeUpdateDateView(UpdateView):
    model = Resume

    def post(self, request, *args, **kwargs):
        resume = Resume.objects.get(id=kwargs['pk'])
        resume.updated_at = datetime.now()
        resume.save()
        return redirect('account_detail', resume.author.username)

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().author == request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class DeleteResumeView(DeleteView):
    model = Resume
    success_url = '/'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().author == request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)






class ResumePublicView(UpdateView):
    model = Resume

    def post(self, request, *args, **kwargs):
        resume = Resume.objects.get(id=kwargs['pk'])
        if resume.is_public:
            resume.is_public = False
            resume.save()
            return redirect('account_detail', resume.author.username)
        if not resume.is_public:
            resume.is_public = True
            resume.save()
        return redirect('account_detail', resume.author.username)




