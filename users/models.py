from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.

class Writer(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


student_group = Group.objects.get(name='Students')
teacher_group = Group.objects.get(name='Teachers')
judge_group = Group.objects.get(name='Judges')
mentor_group = Group.objects.get(name='Mentors')
admin_group = Group.objects.get(name='Admins')


