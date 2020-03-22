from django.db import models

# Create your models here.

class NahibuClient(models.Model):
    kitNumber=models.CharField(max_length=300,primary_key=True)
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    mail=models.EmailField()
    results=models.CharField(max_length=200,default="nolink")
    def __str__(self):
        return self.kitNumber

class Result(models.Model):
    kitNumber = models.CharField(max_length=300)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
