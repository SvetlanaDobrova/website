from django import forms
from django.forms import ModelForm
from catalog.models import Feedback
class feedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['feedbackDate']
        labels = {
            "Username": "Имя",
            "Rating": "Рейтинг",
            "Text": "Отзыв"
        }
    '''
    userContactData = forms.CharField(label="Телефон", max_length=20)
    userName = forms.CharField(label="Имя", max_length=20)
    '''