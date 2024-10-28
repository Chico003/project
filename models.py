from django.db import models

class Member(models.Model):
	name = models.Charfield(max_length=100)
	position = models.Charfield(max_length=50)

class Event(models.Model):
	name = models.Charfield(max_length=100)
	date = models.DateField()
	details = models.TextField()

class Project(models,Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='projects/')
	created_at = models.DateTimeField(auto_now_add=True)
