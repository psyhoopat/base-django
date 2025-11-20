from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField() # имя файла
    cover = models.ImageField(upload_to='images/') # путь к файлу
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    ) # кто пользователь

    def __str__(self):
        return self.title # каждая запись будет именовано пользовательским вводом