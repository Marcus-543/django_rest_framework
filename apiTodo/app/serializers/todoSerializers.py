from rest_framework import serializers
from app.serializers.userSerializers import UserSerializer
from app.models.todoModel import Todo

class TodoSerializer(serializers.ModelSerializer):
    userInfo = UserSerializer(source='userId', read_only=True)

    class Meta:
        model = Todo
        fields = ['id', 'name', 'done', 'created_at', 'userInfo', 'userId']
        extra_kwargs = {
            'userId': {'write_only': True},
        }  