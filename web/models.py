from django.db import models


class Questions(models.Model):
    question = models.CharField(max_length=3000)
    answer1 = models.CharField(max_length=200)
    answer2 = models.CharField(max_length=200)
    answer3 = models.CharField(max_length=200)
    answer4 = models.CharField(max_length=200)
    currect = models.CharField(max_length=200)
    best_score = models.CharField(max_length=3)

    def __str__(self):
        return self.question + ' - ' + self.best_score + ' scores'


class Top(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    best_score = models.CharField(max_length=3)

    def __str__(self):
        return self.name + ' ' + self.surname
