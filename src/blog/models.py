from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField(max_length=50, unique=True)
  slug = models.SlugField(max_length=50, unique=True)

  def __str__(self):
    return self.name

class Series(models.Model):
  title = models.CharField(max_length=50, blank=False)
  slug = models.SlugField(max_length=50, blank=False, default="slug/")

  def __str__(self):
    return self.title



class Post(models.Model):
  title = models.CharField(max_length=150)
  tags = models.ManyToManyField('Tag', blank=True)
  body_markdown=models.TextField(blank=False)
  is_published=models.BooleanField(default=False)
  # series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True, default="")
  slug = models.SlugField(max_length=100, blank=False, default="slug/")

  def __str__(self):
    return self.title

