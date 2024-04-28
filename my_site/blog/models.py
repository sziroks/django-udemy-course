from django.db import models
from django.utils.text import slugify
# Create your models here.


class Author(models.Model):
    id_author = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    date = models.DateField(null=False)
    author = models.ForeignKey(Author(), on_delete=models.CASCADE, null=False)
    slug = models.SlugField(max_length=100, null=False, db_index=True)
    image = models.ImageField(upload_to="images")
    excerpt = models.TextField(null=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    id_comment = models.AutoField(primary_key=True)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, related_name="comments")
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
