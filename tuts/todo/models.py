from django.db import models

# Create your models here.
class Todo(models.Model):
    date_added = models.DateTimeField('date published')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text



