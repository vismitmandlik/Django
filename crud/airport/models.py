from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(_MAX_LENGTH=30)
    desc = models.CharField(_MAX_LENGTH=50)