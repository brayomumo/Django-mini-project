from django.test import TestCase
from .models import Article,Editor,Tags
import datetime as dt

# Create your tests here.
class EditorTestCase(TestCase):
    def setUp(self):
        self.james = Editor(first_name = 'James', last_name='kinuthuia', email= 'jamesKinutia@gmail.com')

    #Testing instance 
    def test_instance(self):
        self.assertTrue(isinstance(self.james, Editor))

    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    # def test_delete_method(self):
    #     self.james.delete_editor()
    #     editors = Editor.objects.all()
    #     self.assertTrue(len(editors) > 0)


class ArticleTestClass(TestCase):
    
    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = Tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_today(self):
        test_date = '2019-08-18'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
       


    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

class TagsTestCase(TestCase):

    def setUp(self):
        self.tag1 = Tags(name = "kitag")

    #Testing instance 
    def test_instance(self):
        self.assertTrue(isinstance(self.tag1, Tags))

    def test_save_tag_method(self):
        self.tag1.save()
        kitag = Tags.objects.all()
        self.assertTrue(len(kitag)> 0)