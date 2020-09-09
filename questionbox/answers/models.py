from django.db.models import Model, DateField, IntegerField, TextField, ForeignKey, CASCADE
from users.models import User

# Create your models here.
class Answer(Model):
    User = ForeignKey(User, related_name="answers", on_delete=CASCADE)
    answer_body = TextField("Place your response here", null=False, blank=False, max_length=2500)
    answer_date = DateField(auto_now_add=True, blank=False, null=False)
    answer_rank = IntegerField()
