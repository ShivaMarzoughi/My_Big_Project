from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from courses.models import CoursesCardModel


# class HomeView(TemplateView):
#     template_name = 'home.html'  


class HomeView(ListView):
    model=CoursesCardModel
    template_name='home.html'
    context_object_name = 'courses_list'

# class HomeView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['courses_list'] = CoursesCardModel.objects.all()  # گرفتن تمام دوره‌ها از مدل
#         return context