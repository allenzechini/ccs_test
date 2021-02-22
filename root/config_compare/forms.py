from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re

class CompareConfigForm(forms.Form):
    first_file_field = forms.FilePathField(
        path=f'{settings.MEDIA_ROOT}\\uploads\\', 
        recursive=True, 
        match=r'\.js(on)?$'
    )
    second_file_field = forms.FilePathField(
        path=f'{settings.MEDIA_ROOT}\\uploads\\', 
        recursive=True, 
        match=r'\.js(on)?$'
    )

class UploadConfigForm(forms.Form):
    file_field = forms.FileField(
        label='New Configuration File',
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
            }
        ),
    )

    def clean_file_field(self):
        data = self.cleaned_data['file_field'].name
        if re.search(r'\.js(on)?$', data) == None:
            raise ValidationError(_('Invalid file: File extension must be .js or .json'))
        return data