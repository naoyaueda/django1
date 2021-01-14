from django.db import models

# Create your models here.

class School(models.Model):
    school_name = models.TextField()
    description = models.TextField()
    courses     = models.TextField()
    fees        = models.TextField()