from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True)
    #파이썬 세상에서 sql세상으로 가기전에 migrations