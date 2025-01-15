from django.urls import path 
from .views import QuestionView



urlpatterns = [
    path('Questions/',QuestionView.as_view(),name='Questions')
]