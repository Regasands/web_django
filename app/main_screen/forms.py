from django import forms
from app.main_screen.models import PollInfoModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Div, Button, Fieldset, HTML, Column


class PollCreateForm(forms.ModelForm):
    class Meta:
        model = PollInfoModel
        fields = ('types', 'poll_name', 'topic', 'max_vote',)

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        print('fff')