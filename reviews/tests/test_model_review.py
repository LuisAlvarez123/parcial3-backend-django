from django.contrib.auth import get_user_model, get_user
from django.test import TestCase
from reviews.models import Review, Movie, Category

class ReviewModelTest(TestCase):    

    @classmethod    
    def setUpTestData(cls):
        category = Category.objects.create(name = 'Terror',color= '#ffffff')
        movie = Movie.objects.create(poster='', movieName='venom', description='entretenida', category=category)
        userSave = get_user_model()(username='luis', first_name='Luis ', last_name='alvarez')
        userSave.set_password('luis')
        userSave.save()

        Review.objects.create(comment='Es muy buena la pelicula la verdad', ranking=4, movie=movie, user=userSave)
        pass

    def test_comment_label(self):
        data = Review.objects.get(id=1)
        field_label = data._meta.get_field('comment').verbose_name        
        self.assertEquals(field_label,'comment')
    
    def test_ranking_label(self):
        data = Review.objects.get(id=1)
        field_label = data._meta.get_field('ranking').verbose_name        
        self.assertEquals(field_label,'ranking')
    
    def test_comment_value(self):
        data = Review.objects.get(id=1)         
        self.assertEquals(data.comment,'Es muy buena la pelicula la verdad')
    
    def test_ranking_value(self):
        data = Review.objects.get(id=1)         
        self.assertEquals(data.ranking, 4)
    
    def test_related_movieName_value(self):
        data = Review.objects.get(id=1)         
        self.assertEquals(data.movie.movieName, 'venom')
    
    def test_related_username_value(self):
        data = Review.objects.get(id=1)         
        self.assertEquals(data.user.username, 'luis')
    

