from django import forms
from django.conf import settings

class UploadConfigForm(forms.Form):
    file_field = forms.FileField(
        label='New Configuration File',
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
            }
        ),
    )

class CompareConfigForm(forms.Form):
    first_file_field = forms.FilePathField(
        path=f'{settings.MEDIA_ROOT}\\uploads\\', 
        recursive=True, 
        match=r'js(on)?$'
    )
    second_file_field = forms.FilePathField(
        path=f'{settings.MEDIA_ROOT}\\uploads\\', 
        recursive=True, 
        match=r'js(on)?$'
    )