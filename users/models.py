from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.

student_group = Group.objects.get(name='Students')
teacher_group = Group.objects.get(name='Teachers')
judge_group = Group.objects.get(name='Judges')
mentor_group = Group.objects.get(name='Mentors')
admin_group = Group.objects.get(name='Admins')


class Student(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    # gender = models.CharField(max_length=100)
    excited = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    book = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    # publication_date = models.DateField()

    def __str__(self):
        return self.f_name


