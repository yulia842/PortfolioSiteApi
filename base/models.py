from django.db import models
from django.core.validators import EmailValidator

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(validators=([EmailValidator()]))
    message = models.CharField(max_length=600)
