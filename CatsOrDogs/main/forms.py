from django import forms
from .models import Picture


class UploadFileForm(forms.Form):
    file = forms.FileField()