from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()
    

    class Meta:
        ordering = ['first_name']

class Tags(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 60)
    post = models.TextField()
    editor = models.ForeignKey(
        Editor,
        on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_article(self):
        self.save()

    # def delete_editor(self):
    #     self.delete()

    def delete_Article(self):
        self.delete()