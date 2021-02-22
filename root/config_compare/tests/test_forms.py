from django.test import TestCase
from config_compare.forms import CompareConfigForm, UploadConfigForm
from django.conf import settings

# Create your tests here. 
class ConfigCompareFormTest(TestCase):
    def test_form_field_paths(self):
        form = CompareConfigForm()
        self.assertTrue(form.fields['first_file_field'].path == f'{settings.MEDIA_ROOT}\\uploads\\')
        self.assertTrue(form.fields['second_file_field'].path == f'{settings.MEDIA_ROOT}\\uploads\\')

    def test_form_field_recursiveness(self):
        form = CompareConfigForm()
        self.assertTrue(form.fields['first_file_field'].recursive == True)
        self.assertTrue(form.fields['second_file_field'].recursive == True)

    def test_form_field_matching(self):
        form = CompareConfigForm()
        self.assertTrue(form.fields['first_file_field'].match == r'\.js(on)?$')
        self.assertTrue(form.fields['second_file_field'].match == r'\.js(on)?$')

    # def test_one_bad_extention(self):
    #     form = CompareConfigForm(data={
    #         'first_file_field': f'{settings.MEDIA_ROOT}\\uploads\\test_file.fail',
    #         'second_file_field': f'{settings.MEDIA_ROOT}\\uploads\\test_file.json',
    #     })
    #     self.assertFalse(form.is_valid())
    
    # def test_two_bad_extentions(self):
    #     form = CompareConfigForm(data={
    #         'first_file_field': f'{settings.MEDIA_ROOT}\\uploads\\test_file.fail',
    #         'second_file_field': f'{settings.MEDIA_ROOT}\\uploads\\test_file.fail',
    #     })
    #     self.assertFalse(form.is_valid())

    # def test_two_good_extentions(self):
    #     form = CompareConfigForm(data={
    #         'first_file_field': 'test_file.json',
    #         'second_file_field': 'test_file.js',
    #     })
    #     self.assertTrue(form.is_valid())

class UploadConfigFormTest(TestCase):
    def test_upload_form_label(self):
        form = UploadConfigForm()
        self.assertTrue(
            form.fields['file_field'].label == None or 
            form.fields['file_field'].label == 'New Configuration File'
        )
