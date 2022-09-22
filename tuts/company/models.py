from django.db import models

# Create your models here.
class company(models.Model):
    name =models.CharField(max_length=50)
    location = models.TextField()

    def __str__ (self):
        return self.name
