from django.contrib import admin
from .models import Teacher_of_course,CoursesCardModel,Course_Details,VideosOfLesson
# Register your models here.
admin.site.register(VideosOfLesson)
admin.site.register(Course_Details)
admin.site.register(CoursesCardModel)
admin.site.register(Teacher_of_course)
