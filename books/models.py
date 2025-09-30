from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=155, verbose_name='Назва')
    author = models.CharField(max_length=80, verbose_name='Автор')
    year = models.IntegerField(verbose_name='Рік видання', default=0)

    def __str__(self):
        return f'{self.title} - {self.author}'