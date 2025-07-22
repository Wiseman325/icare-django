from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Case(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE) # foreign key to user
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=200)
    case_type = models.ForeignKey('CaseType', on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    status_reason = models.TextField(max_length=2500, blank=True, null=True)

    class Meta:
        ordering = ['-updated_at', '-submitted_at']

    def __str__(self):
        return self.title
     
class CaseType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name 

class roomForum(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    room = models.ForeignKey(roomForum, on_delete=CASCADE)
    body = models.TextField(max_length=5000)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.body[0:50]  # Return first 50 characters of the message body
