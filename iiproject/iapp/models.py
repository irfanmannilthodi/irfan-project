from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()
class Background(models.Model):
    img=models.ImageField(upload_to="pics")

class Open(models.Model):
    img=models.ImageField(upload_to="pics")
class Choose(models.Model):
    img=models.ImageField(upload_to="pics")

class three(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()

    # def __str__(self):
    #     return self.name
