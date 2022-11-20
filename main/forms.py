from django import forms

from main.models import Message

class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)
        