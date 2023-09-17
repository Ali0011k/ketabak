from django.test import TestCase
from books.models import *
from django.test import TestCase


class BookModelTest(TestCase):
    
    def setUp(self):
        book = {
            'name':'test book',
            'author' : 'some one',
            'number_of_pages':  100,
            'description' : 'a simple discreption',
            'cover':1
        }
        Book.objects.create(**book)
        
        
    def test_book_exist(self):
        
        book = Book.objects.get(pk = 1)
        all_books = Book.objects.all()
        self.assertIn(book , all_books)
        
        
    def test_book_equal(self):

        book = Book.objects.get(pk = 1)
        self.assertEqual(book.name , 'test book')
        
        
        


