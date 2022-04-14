from django.contrib import admin

# Register your models here.
from .models import Tag, Series, Post

admin.site.register(Tag)
admin.site.register(Series)
admin.site.register(Post)
