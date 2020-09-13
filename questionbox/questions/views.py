from django.views.generic.detail import DetailView
from Django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question, Answer

class view_question(DetailView):
    model = Question
    template_name = "questions/view_question.html"

class view_answer(DetailView):
    model = Answer
    template_name = "answers/view_answer.html"

class create_question(CreateView):
    model = Question
    template_name = "create_question.html"

class create_answer(CreateView):
    model = Answer
    template_name = "create_answer.html"

class edit_question(UpdateView):
    model = Question
    template_name = "edit_question.html"

class edit_answer(UpdateView):
    model = Answer
    template_name = "edit_answer.html"

class delete_question(DeleteView):
    model = Question
    template_name = "delete_question.html"

class delete_answer(DeleteView):
    template_name = "delete_answer.html"