from django.db import models

# Create your models here.

class task(models.Model):
    name = models.CharField(max_length=50)
    deadline = models.DateField()
    assignee = models.CharField(max_length=50)

    def __str__(self):
        return self.name