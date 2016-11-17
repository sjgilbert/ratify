from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer_text = models.CharField(max_length=200)
	num_votes = models.IntegerField(default=0)