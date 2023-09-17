from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('' , home),
    path('home/' , home , name='home'),
    path('language/' , switch_language , name='switch language')

]