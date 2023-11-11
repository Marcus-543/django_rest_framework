from rest_framework import viewsets

from app.models.userModel import User
from app.serializers.userSerializers import UserSerializer

class UserViewsSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer