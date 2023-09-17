from django.urls import path
from api.views import *

app_name = 'api'

urlpatterns = [
    path('data/content/books/' , book_list_and_create , name='book_list_and_create'),
    path('data/content/books/update/' , book_update , name='book_update'),
]