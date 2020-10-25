from sapujagad.core.utils import FilenameGenerator
from django.db import models


class Contactus(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=25)
    message = models.TextField(max_length=254)

    def __str__(self):
        return self.name