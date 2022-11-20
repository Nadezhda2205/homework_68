from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from main.forms import ResumeForm, EducationForm
from main.models import Resume, Education, Experience


class AddEducationView(CreateView):
    template_name = 'add_education.html'
    form_class = EducationForm
    model = Education
    success_url = '/'

    def form_valid(self, form):
        resume = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        education = form.save(commit=False)
        education.resume = resume
        education.save()
        return redirect('edit_resume', pk=resume.pk)

    def get_context_data(self, *args, **kwargs):
        context = super(AddEducationView, self).get_context_data()
        context['resume'] = get_object_or_404(Resume, pk=self.kwargs.get('pk'))
        return context


class EditEducationView(UpdateView):
    template_name = 'edit_education.html'
    form_class = EducationForm
    model = Education

    def get_context_data(self, **kwargs):
        context = super(EditEducationView, self).get_context_data()
        education = Education.objects.get(id=self.object.id)
        context['resume'] = education.resume
        print(education.resume)
        return context

    def get_success_url(self):
        education = Education.objects.get(id=self.object.id)
        return reverse_lazy('edit_resume', kwargs={'pk': education.resume.pk})


class DeleteEducationView(DeleteView):
    model = Education

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        education = Education.objects.get(id=self.object.id)
        return reverse_lazy('edit_resume', kwargs={'pk': education.resume.pk})