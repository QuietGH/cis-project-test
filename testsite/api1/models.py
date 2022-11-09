from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length = 20)
    length = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()

    def _str_(self):
        return self.name

    def get_length(self):
        return self.length