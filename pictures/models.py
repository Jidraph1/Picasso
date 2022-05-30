from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=60)
    
    def __str__(self):
        """
    A method that returns a location as a string
     """
        return self.location 
    
    def save_location(self):
        """
    A method that saves a location
     """
        self.save()
    
    def delete_location(self):
        """
    A method that deletes a location
     """
        self.delete()
    
    class Meta:
        ordering = ['location']


class categories(models.Model):
    category = models.CharField(max_length=60)
     
    def __str__(self):
        """
    A method that returns a category as a string
     """
        return self.category    
    
    def save_category(self):
        """
    A method that saves a category
     """
        self.save()
    
    def delete_category(self):
        """
    A method that deletes a category
     """
        self.delete()
    
    class Meta:
        ordering = ['category']   


class Image(models.Model):
    image= 

