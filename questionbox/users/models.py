from django.db import models
from django.contrib.auth.models import AbstractUser
"""from django.views.generic import Listiew"""

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    pass
    

class Question(models.Model):
    template_name = 'create_question.html'
    user_question = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    question_title = models.CharField("What kind of question is this?", null=False, blank=False, max_length=200)
    question_body = models.CharField("Write your question here", null=False, blank=False, max_length=2500)
    question_date = models.DateField()

class Answer(models.Model):
    template_name = 'create_answer.html'
    user_answer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    answer_body = models.CharField("Place your response here", null=False, blank=False, max_length=2500)
    answer_date = models.DateField(auto_now_add=True, blank=False, null=False)
    answer_rank = models.IntegerField()

