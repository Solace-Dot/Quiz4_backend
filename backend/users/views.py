from rest_framework import generics

from users.permissions import IsAdmin
from users.serializers import UserCreateSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [IsAdmin]
