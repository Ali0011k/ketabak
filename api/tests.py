from django.test import TestCase
from rest_framework.test import APIClient
from books.models import *


class BookAPITest(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            "name": "کتاب تستی",
            "author": "علی خانی",
            "number_of_pages": 100,
            "description": "<p>اطلاعات کتاب تستی</p>",
            "create_time": "2023-09-16",
            "cover": 1
        }
        self.book = Book.objects.create(**self.book_data)


    def test_get_method(self):
        url = "/api/data/content/books/update/?id={}".format(self.book.pk)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "کتاب تستی")


    def test_post_method(self):
        new_book_data = {
            "name": "کتاب جدید",
            "author": "نویسنده جدید",
            "number_of_pages": 150,
            "description": "<p>اطلاعات کتاب جدید</p>",
            "create_time": "2023-09-17",
            "cover": 2
        }
        url = '/api/data/content/books/'
        response = self.client.post(url, new_book_data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Book.objects.filter(name="کتاب جدید").exists())


    def test_update_method(self):
        updated_data = {
            "name": "کتاب به روز رسانی شده",
            "author": "نویسنده بروز رسانی شده",
            "number_of_pages": 150,
            "description": "<p>اطلاعات کتاب به روز زسانی شده</p>",
            "create_time": "2023-09-17",
            "cover": 2
        }
        url = "/api/data/content/books/update/?id={}".format(self.book.pk)
        
        response = self.client.put(url, updated_data, format="json")


        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.name, "کتاب به روز رسانی شده")
        self.assertEqual(self.book.number_of_pages, 150)

    def test_delete_method(self):
        url = "/api/data/content/books/update/?id={}".format(self.book.pk)
        
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())
