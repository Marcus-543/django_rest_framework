from rest_framework import serializers
from app.models.todoModel import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'done', 'created_at']