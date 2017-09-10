from django.db import models

# Create your models here.

GENDER = (
    ('M', 'men'),
    ('W', 'women')
)


class Student(models.Model):
    name = models.CharField(max_length=50, default='张三')
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=5, choices=GENDER)

