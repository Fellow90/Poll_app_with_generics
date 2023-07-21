import datetime
from django.db import models
from django.contrib import admin

from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Published Date:")

    def __str__(self):
        return f"Question : {self.question_text}"
    

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - timezone.timedelta(days = 1)
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        return (
            timezone.now()
            >= self.pub_date
            >= timezone.now() - timezone.timedelta(days=1)
        )


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(default="Nothing")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"Choice : {self.choice_text}"
