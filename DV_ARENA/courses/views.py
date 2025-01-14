from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import CoursesCardModel , Course_Details




class CoursesView(ListView):
    model=CoursesCardModel
    # template_name='courses_card.html'
    template_name='home.html'
    context_object_name = 'courses_list'


class CoursesDetailView(DetailView):
    model=CoursesCardModel
    template_name='courses_datail.html'
    context_object_name='courses_detail_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # فیلتر کردن سرفصل‌ها برای دوره جاری
        course_details = Course_Details.objects.filter(name_of_course=self.object)
        context['course_details'] = course_details
        # course_card=CoursesCardModel.objects.all()
        # context['course_card']=course_card

        context['course_card'] = self.object
        return context


    # این روش کاربرد نداشت
    # model=Course_Details
    # template_name='courses_datail.html'
    # context_object_name='courses_detail_list'






