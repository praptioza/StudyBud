from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)   # null values are allowed for this column and when the form is submitted, this field can be blank so it can be saved as blank field
    # participants = 
    updated = models.DateTimeField(auto_now=True) # so whenever the save method is called, take a snapshot / timestamp and store it in the database column 'updated'
    created = models.DateTimeField(auto_now_add=True) # this takes only a timestamp when it is saved for the first time and not everytime you save the same instance


    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.body[0:50]