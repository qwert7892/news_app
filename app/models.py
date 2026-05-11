from django.db import models
from django.contrib.auth.models import AbstractUser, User


# class User(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     login = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     phone = models.CharField(max_length=20)
#     password = models.CharField(max_length=200)


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    summary = models.CharField(max_length=300, verbose_name="Краткое описание")
    content = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
