from django.db import models
import datetime


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    # date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name
