from django.test import TestCase
from .models import Location, categories, Image
# Create your tests here.

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.James= Image(id = '1', image = 'example.jpg', name = 'James', description ='This is one of my favourite photos', location ='Nairobi', categories ='Portrait')