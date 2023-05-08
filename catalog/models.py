from django.db import models

class BeautyService(models.Model):
    Name = models.CharField(max_length=100)
    Duration = models.DurationField()
    Price = models.DecimalField(max_digits=7, decimal_places=2)
    Description = models.TextField()
    Photo = models.ImageField(upload_to='pics')
