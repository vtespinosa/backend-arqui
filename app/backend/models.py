from django.db import models

# Create your models here.

class User(models.Model):
  nickname = models.CharField(max_length=100)

  def __str__(self):
    return self.nickname

class Room(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Message(models.Model):
  text = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add=True)
  nickname = models.CharField(max_length=100)
  room = models.CharField(max_length=100)
  censored = models.BooleanField(default=False)

  def __str__(self):
    return self.text
