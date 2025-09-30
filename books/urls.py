from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='book_list'),
    path('book/detail/<int:id>/', views.book_detail, name='book_detail'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/update/<int:id>/', views.book_update, name='book_update'),
    path('book/delete/<int:id>/', views.book_delete, name='book_delete')
]