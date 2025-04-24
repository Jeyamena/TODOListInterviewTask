from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the task is created
    updated_at = models.DateTimeField(auto_now=True)      # Automatically set when the task is updated

    def __str__(self):
        return self.name
