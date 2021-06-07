from django.urls import path
from .views import *

urlpatterns = [
    path('question/<int:poll_id>/',question_page,name='questions')
]