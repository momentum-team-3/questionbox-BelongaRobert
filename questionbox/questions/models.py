from django.db import Model, CharField, TextField, ManyToManyField, ForeignKey, CASCADE
from users.models import User


# Create your models here.
class Question(Model):
    User = Model.ForeignKey(User, on_delete=CASCADE, related_name="questions")
    question_title = CharField("What kind of question is this?", null=False, blank=False, max_length=200)
    question_body = TextField("Write your question here", null=False, blank=False, max_length=2500)
    question_date = DateTimeField()
    tags = ManyToManyField("Tag")