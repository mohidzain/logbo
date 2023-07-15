from django.db import models
from django.contrib.auth.models import Group, User
from PIL import Image

# Create your models here.

student_group = Group.objects.get(name='Students')
teacher_group = Group.objects.get(name='Teachers')
judge_group = Group.objects.get(name='Judges')
mentor_group = Group.objects.get(name='Mentors')
admin_group = Group.objects.get(name='Admins')

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    # gender = models.CharField(max_length=100)
    excited = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    book = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    # avatar = models.ImageField(default='default.png', upload_to='profile_images')

    # resizing images
    # def save(self, *args, **kwargs):
    #     super().save()
    #     img = Image.open(self.avatar.path)
    #     if img.height > 100 or img.width > 100:
    #         new_img = (100, 100)
    #         img.thumbnail(new_img)
    #         img.save(self.avatar.path)

    def __str__(self):
        return self.f_name

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='abcd', upload_to='profile_images')
    bio = models.TextField()
    # resizing images
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
    def __str__(self):
        return self.user.username
    

