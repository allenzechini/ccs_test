from django.test import TestCase
from django.urls import reverse
from config_compare.models import ConfigurationFile
from config_compare.forms import CompareConfigForm, UploadConfigForm

# Create your tests here.
class CompareConfigViewTest(TestCase):
    def test_compare_view_url_exists_at_desired_location(self):
        response = self.client.get('/config_compare/compare.html')
        self.assertEqual(response.status_code, 200)

    def test_compare_view_url_accessible_by_name(self):
        response = self.client.get(reverse('compare_config'))
        self.assertEqual(response.status_code, 200)

    def test_compare_view_uses_correct_template(self):
        response = self.client.get(reverse('compare_config'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'compare.html')

    def test_copmare_success_view_url_exists_at_desired_location(self):
        response = self.client.get('/config_compare/compare_success.html')
        self.assertEqual(response.status_code, 200)

    def test_compare_success_view_url_accessible_by_name(self):
        response = self.client.get(reverse('compare_success'))
        self.assertEqual(response.status_code, 200)

    def test_compare_success_view_uses_correct_template(self):
        response = self.client.get(reverse('compare_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'compare_success.html')

class UploadConfigViewTest(TestCase):
    def test_upload_view_url_exists_at_desired_location(self):
        response = self.client.get('/config_compare/upload.html')
        self.assertEqual(response.status_code, 200)

    def test_upload_view_url_accessible_by_name(self):
        response = self.client.get(reverse('upload_config'))
        self.assertEqual(response.status_code, 200)

    def test_upload_view_uses_correct_template(self):
        response = self.client.get(reverse('upload_config'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload.html')

    def test_upload_success_view_url_exists_at_desired_location(self):
        response = self.client.get('/config_compare/upload_success.html')
        self.assertEqual(response.status_code, 200)

    def test_upload_success_view_url_accessible_by_name(self):
        response = self.client.get(reverse('upload_success'))
        self.assertEqual(response.status_code, 200)

    def test_compare_success_view_uses_correct_template(self):
        response = self.client.get(reverse('upload_success'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'upload_success.html')
