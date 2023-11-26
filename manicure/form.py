

from django import forms

from manicure.models import Album, Category


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class AddCat(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
    