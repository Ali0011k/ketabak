from django.test import TestCase


class ReactTest(TestCase):
    
    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code , 200)
        
        
    def test_redirect_code(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code , 200)