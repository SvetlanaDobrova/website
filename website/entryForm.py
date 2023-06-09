from django import forms
from django.forms import ModelForm, Textarea
from catalog.models import Contacts
class entryForm(forms.ModelForm):
    class Meta:
        model = Contacts
        exclude = ['contactTimeStamp']
        labels = {
        "userName": "Имя",
        "userContactData": "Номер телефона"
             }

    '''
    userContactData = forms.CharField(label="Телефон", max_length=20)
    userName = forms.CharField(label="Имя", max_length=20)
    '''