from django.views.generic.detail import DetailView
from Django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Question, Answer

class view_question(DetailView):
    model = Question
    template_name = "questions/view_question.html"

class view_answer(DetailView):
    model = Answer
    template_name = "answers/view_answer.html"