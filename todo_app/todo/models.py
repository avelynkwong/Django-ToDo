from django.db import models

# Create your models here.
class TodoItem(models.Model): #represents each todo item
    content = models.TextField()