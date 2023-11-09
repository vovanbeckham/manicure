

from django import forms

from manicure.models import Album


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
    