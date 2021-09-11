from django.db import models

# Create your models here.

class Jobsite(models.Model):
    class Meta:
        verbose_name = "Jobsite"
        verbose_name_plural = "Jobsites"
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Sundry(models.Model):
    class Meta:
        verbose_name = "Sundry"
        verbose_name_plural = "Sundries"
    name = models.CharField(max_length = 100)
    quantity_available = models.IntegerField()
    def __str__(self):
        return self.name
        
class Equipment(models.Model):
    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment"
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length = 100)
    jobsite = models.CharField(max_length = 200)
    date_needed = models.DateField()
    # possible future implementation: distance_to_jobsite = models.FloatField()

    def __str__(self):
        return self.name + " - " + self.jobsite
 
class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    text = models.CharField(max_length = 300)
    quantity_requested = models.IntegerField(default=0)

    def __str__(self):
        return self.text 

