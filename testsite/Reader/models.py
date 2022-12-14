from django.db import models

# Create your models here.

class Substance(models.Model):
    PubChem_Name = models.CharField(max_length = 50)
    PubChem_Alias = models.CharField(max_length = 50)
    PubChem_CID = models.IntegerField(primary_key = True)
    PubChem_Mass = models.FloatField()
    PubChem_Formula = models.CharField(max_length = 50)
    Local_Image = models.ImageField(default = './default_image.jpg')
    Local_Subcategory = models.TextChoices('Subgroup','DRUGS PROTEINOGENICAMINOACIDS')
