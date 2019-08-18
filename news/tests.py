from django.test import TestCase
from .models import Article,Editor,Tags

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


# class ArticleTestCase(TestCase):
#     def setUp(self):
#         self.article1 = Article(title = 'news1', post = 'Making it happen at Moringa Get informed')

#     #Test instance 
#     def test_instance(self):
#         self.assertTrue(isinstance(self.article1, Article))

#     def test_save_method(self):
#         self.article1.save_article()
#         article = Article.objects.all()
#         self.assertTrue(len(article) > 0)


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