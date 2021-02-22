from django.db import models

"""
ConfigurationFile class:
    Model allowing for a configuration file to be uploaded
"""
class ConfigurationFile(models.Model):
    configuration_file = models.FileField(
        upload_to="uploads/", 
        help_text='Enter the name of a configuration file'
    )
    pub_date = models.DateTimeField(
        'Date Published',
        auto_now=True,
    )

    # String for representing the ConfigurationFile object (in Admin site, etc.)
    def __str__(self):
        return f'{self.configuration_file}'

class Meta:
    ordering = ['pub_date']