from django import forms
from .models import UploadFile
from django.core.files.storage import default_storage


class SingleUploadModelForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = '__all__'
