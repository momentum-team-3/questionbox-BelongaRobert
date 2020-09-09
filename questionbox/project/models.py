


class Question(models.Model):
    user_question = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    question_title = models.CharField("What kind of question is this?", null=False, blank=False, max_length=200)
    question_body = models.CharField("Write your question here", null=False, blank=False, max_length=2500)
    question_date = models.DateField()