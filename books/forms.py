from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year']
        labels = {
            'title' : 'Назва книги',
            'author' : 'Автор книги',
            'year' : 'Рік видання книги'
        }
        help_texts = {
            'title' : 'Введіть назву книги',
            'author' : 'Введіть автора книги',
            'year' : 'Введіть рік видання книги'
        }