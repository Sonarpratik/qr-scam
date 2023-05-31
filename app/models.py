from django.db import models



class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=50)



class Question(models.Model):
    title=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    created_by=models.CharField(max_length=50)


class Choices(models.Model):
    question=models.CharField(max_length=50)
    text=models.CharField(max_length=50)