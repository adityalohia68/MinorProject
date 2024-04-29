from django.db import models

# Create your models here.
class BookAppointment(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    state = models.CharField(max_length=20)
    date = models.DateTimeField(blank=True, null=True)
