from django.db.models import Model, CharField, TextField, ManyToManyField, DateField, ForeignKey, IntegerField, CASCADE
from users.models import User


# Create your models here.
class Question(Model):
    question_of = ForeignKey(User, on_delete=CASCADE, related_name="questions")
    question_title = CharField("What kind of question is this?", null=False, blank=False, max_length=200)
    question_body = TextField("Write your question here", null=False, blank=False, max_length=2500)
    question_date = DateField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return 
        {
            self.question_body,
            self.question_date,
            self.question_of,
            self.question_title,
        }

class Answer(Model):
    answer_of = ForeignKey(User, related_name="answers", on_delete=CASCADE)
    answer_body = TextField("Place your response here", null=False, blank=False, max_length=2500)
    answer_date = DateField(auto_now_add=True, blank=False, null=False)
    answer_rank = IntegerField()

    def __str__(self):
        return 
        {
            self.answer_body,
            self.answer_date,
            self.answer_of,
            self.answer_rank,
        }
