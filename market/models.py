from django.db import models

# Create your models here.
class Contact2(models.Model):
    email = models.EmailField('email', max_length=255)
    name = models.TextField('name')
    address = models.TextField('address')
    message = models.TextField('message')

    sent_at = models.DateTimeField(auto_now_add=True)