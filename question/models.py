from django.contrib.auth.models import User
from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    text = models.CharField(max_length=70)
    answer = models.CharField(max_length=50)


class UserToPoll(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)