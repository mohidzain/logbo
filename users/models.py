from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.

student_group = Group.objects.get(name='Students')
teacher_group = Group.objects.get(name='Teachers')
judge_group = Group.objects.get(name='Judges')
mentor_group = Group.objects.get(name='Mentors')
admin_group = Group.objects.get(name='Admins')


