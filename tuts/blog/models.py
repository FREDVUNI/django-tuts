from django.db import models

# Create your models here.
class article(models.Model):
    reporter =models.CharField(max_length=50)
    article =models.TextField()

    def __str__(self):
        return self.reporter

