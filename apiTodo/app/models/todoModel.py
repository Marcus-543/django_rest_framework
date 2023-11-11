from django.db import models

from app.models.userModel import User

class Todo(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
