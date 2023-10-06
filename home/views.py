from books.models import *
from django.shortcuts import render , redirect
from django.http import HttpResponse
from time import sleep

def home(request):
    books = Book.objects.all()
    return render(request , 'index.html' , {
        'books':books
    })



def switch_language(request):
    previous_url = request.META.get('HTTP_REFERER')
    url = None
    
    if previous_url:
        if '/fa/' in previous_url:
            url = previous_url.replace('/fa/', '/en/')
        elif '/en/' in previous_url:
            url = previous_url.replace('/en/', '/fa/')
    
    if url:
        return redirect(url)
    else:
        return redirect('/en/')  