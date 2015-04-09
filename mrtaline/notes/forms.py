from django import forms
from models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # exclude missing field in form
        exclude = ['geom', 'created', 'is_publish']
