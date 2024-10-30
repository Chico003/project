from django.db import models  # type: ignore

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # Optional image field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)  # Change 'position' to 'role' to match the model
    bio = models.TextField()  # Add this to your form if you want it to be editable

    def __str__(self):
        return self.name

