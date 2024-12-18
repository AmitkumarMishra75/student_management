from django.db import models

# Create your models here.

class Student(models.Model):
    NAME = models.CharField(max_length=32)
    QUALIFICATION = models.CharField(max_length=32)
    GENDER = models.CharField(max_length=32)
    YOP = models.IntegerField()
    AGE = models.IntegerField()
    SKILLS = models.CharField(max_length=32)
    DOB = models.DateField()
    ADDRESS = models.CharField(max_length=32)
    MOCK_RATING = models.CharField(max_length=32)
    DEPARTMENT = models.CharField(max_length=32)

    def __str__(self):
        return self.NAME