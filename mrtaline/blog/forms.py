from django.forms import ModelForm
from models import Entry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit


class EntryForm(ModelForm):
    class Meta:
        model = Entry


class CREntryForm(EntryForm):
    def __init__(self, *args, **kwargs):
        super(CREntryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'body',
            'publish',
            'authors',
            ButtonHolder(
                Submit('register', 'Register',
                       css_class='btn waves-effect waves-light')
            )
        )
