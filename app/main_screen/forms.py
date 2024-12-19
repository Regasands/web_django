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
        max_vote = cleaned_data.get('max_vote')

        if max_vote is not None and max_vote > 1000:  # Исправлено: добавлено двоеточие в конце строки
            print('r')
            self.add_error('max_vote', 'Максимальноек значение не модет быть больше 1000')
        return cleaned_data
