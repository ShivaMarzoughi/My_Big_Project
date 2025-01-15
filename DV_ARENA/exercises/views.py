from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Question

class QuestionView(ListView):
    model=Question
    template_name='exercise.html'
    context_object_name = 'question_list'

    def get_queryset(self):
    # از request.GET برای دسترسی به پارامتر سطح استفاده می‌کنیم
        level = self.request.GET.get('level')
        if level:
            return Question.objects.filter(level=level)
        else:
            return Question.objects.all()