from django.db import models

# Create your models here.
class Libro(models.Model):
    titolo = models.CharField(max_length=200)
    autore = models.CharField(max_length=100)
    data_pubblicazione = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.titolo