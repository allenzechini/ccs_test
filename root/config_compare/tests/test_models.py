from django.test import TestCase
from config_compare.models import ConfigurationFile
import datetime

# Create your tests here.
class ConfigCompareModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ConfigurationFile.objects.create(configuration_file='test_file.fail', pub_date=datetime.date.today()) # FAIL
        ConfigurationFile.objects.create(configuration_file='test_file.json', pub_date=datetime.date.today()) # PASS
        ConfigurationFile.objects.create(configuration_file='test_file.js', pub_date=datetime.date.today()) # PASS

    def test_file_extension(self):
        file1 = ConfigurationFile.objects.get(id=1)
        file2 = ConfigurationFile.objects.get(id=2)
        file3 = ConfigurationFile.objects.get(id=3)
        extension1 = file1.configuration_file.name.split('.')[1]
        extension2 = file2.configuration_file.name.split('.')[1]
        extension3 = file3.configuration_file.name.split('.')[1]
        self.assertNotEqual(extension1, 'js') 
        self.assertNotEqual(extension1, 'json')
        self.assertEqual(extension2, 'json')
        self.assertEqual(extension3, 'js')