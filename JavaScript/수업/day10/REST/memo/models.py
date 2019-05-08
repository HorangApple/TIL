from django.db import models

# Create your models here.
class Memo (models.Model):
    content = models.TextField()