from django import forms

from main.models import Resume, Experience, Education

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name','email','telegram','phone','linkedin','facebook','vacancy_category', 'salary', 'is_public')


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('description', 'begin_at', 'end_at')

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ('company', 'position', 'duties', 'begin_at', 'end_at')


from main.models import Message

class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
        