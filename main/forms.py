from django import forms
from .models import Picture


class ImageFileUploadForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('image',) 

class FileUploadForm(forms.Form):
    file_source = forms.FileField()