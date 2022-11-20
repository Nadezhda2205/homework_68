from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from main.forms import ResumeForm, EducationForm, ExperienceForm
from main.models import Resume, Education, Experience


class AddExperienceView(CreateView):
    template_name = 'add_experience.html'
    form_class = ExperienceForm
    model = Experience
    success_url = '/'

    def form_valid(self, form):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        experience = form.save(commit=False)
        experience.resume = resume
        experience.save()
        return redirect('edit_resume', pk=resume.pk)

    def get_context_data(self, *args, **kwargs):
        context = super(AddExperienceView, self).get_context_data()
        context['resume'] = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        return context


class EditExperienceView(UpdateView):
    template_name = 'edit_education.html'
    form_class = ExperienceForm
    model = Experience

    def get_context_data(self, **kwargs):
        context = super(EditExperienceView, self).get_context_data()
        experience = Experience.objects.get(id=self.object.id)
        context['resume'] = experience.resume
        return context

    def get_success_url(self):
        experience = Experience.objects.get(id=self.object.id)
        return reverse_lazy('edit_resume', kwargs={'pk': experience.resume.pk})


class DeleteExperienceView(DeleteView):
    model = Experience

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        experience = Experience.objects.get(id=self.object.id)
        return reverse_lazy('edit_resume', kwargs={'pk': experience.resume.pk})