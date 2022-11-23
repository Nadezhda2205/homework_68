from django import forms

from main.models import Resume, Experience, Education

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('vacancy_category', 'salary', 'is_public')


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
        

class SearchForm(forms.Form):
    search_т = forms.CharField(required=False, label='')
