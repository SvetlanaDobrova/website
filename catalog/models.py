from django.db import models

import catalog


class BeautyServiceGroup(models.Model):
    Name = models.CharField(max_length=100)

    SortOrder = models.IntegerField
    Description = models.TextField
    def __str__(self):
        return self.Name

class BeautyService(models.Model):
    Name = models.CharField(max_length=100)
    Duration = models.DurationField()
    Price = models.DecimalField(max_digits=7, decimal_places=2)
    Description = models.TextField()
    Photo = models.ImageField(upload_to='pics')
    Group = models.ForeignKey(BeautyServiceGroup, on_delete=models.PROTECT)
    def __str__(self):
        return self.Name

class Feedback(models.Model):
    Username = models.CharField(max_length=100)
    Rating = models.DecimalField(max_digits=1, decimal_places=0)
    Text = models.TextField()
    #Service = models.ForeignKey(BeautyService, on_delete=models.CASCADE)
    feedbackDate = models.DateTimeField(    )

class Contacts(models.Model):
    userContactData = models.CharField(max_length=50)
    userName = models.CharField(max_length=40)
    contactTimeStamp = models.DateTimeField()
