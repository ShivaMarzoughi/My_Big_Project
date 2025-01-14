from django.urls import path
from .views import CoursesView,CoursesDetailView



urlpatterns = [
    path('courses/',CoursesView.as_view(),name='course'),
    path('courses/<int:pk>/',CoursesDetailView.as_view(),name='course_details'),
]