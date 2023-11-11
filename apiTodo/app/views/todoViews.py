from rest_framework import viewsets

from app.models.todoModel import Todo
from app.serializers.todoSerializers import TodoSerializer

class TodoViewsSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer