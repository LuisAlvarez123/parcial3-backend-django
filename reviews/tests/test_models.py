from django.contrib.auth.models import User
from django.test import TestCase
from reviews.models import Category, Movie

class ModelTest(TestCase):    

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name = 'Terror',color= '#ffffff')
        Movie.objects.create(poster = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Feventos.guatemala.com%2Festrenos-cine-series%2Festreno-de-la-pelicula-venom-2-en-cines-de-guatemala-octubre-2021.html&psig=AOvVaw2OsbRVk47ZztjrZDkaYlHi&ust=1638170729190000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCICnstfDuvQCFQAAAAAdAAAAABAD',movieName= 'venom la 2',description="Es una pelicula de marvel", category=category)
        pass
        #test para categoria
    def test_color_max_length(self):
        category=Category.objects.get(id=1)
        max_length = Category._meta.get_field('color').max_length
        self.assertEquals(max_length,20)

    def test_name_max_length(self):
        category=Category.objects.get(id=1)
        max_length = Category._meta.get_field('name').max_length
        self.assertEquals(max_length,20)

            #test para pelicula
    def test_movieName_max_length(self):
        movie=Movie.objects.get(id=1)
        max_length = Movie._meta.get_field('movieName').max_length
        self.assertEquals(max_length,25)

    def test_description_max_length(self):
        movie=Movie.objects.get(id=1)
        max_length = Movie._meta.get_field('description').max_length
        self.assertEquals(max_length,255)   
    
    def test_movieName_label(self):
        data = Movie.objects.get(id=1)
        field_label = data._meta.get_field('movieName').verbose_name        
        self.assertEquals(field_label,'movieName')

    def test_description_label(self):
        data = Movie.objects.get(id=1)
        field_label = data._meta.get_field('description').verbose_name        
        self.assertEquals(field_label,'description')
    


