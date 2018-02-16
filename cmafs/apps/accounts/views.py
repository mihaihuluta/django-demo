from django.conf import settings
from django.contrib.auth import get_user_model
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import generics, exceptions, views, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rest_framework_jwt.settings import api_settings

from .permissions import IsOwnerOrReadOnly
from .serializers import AccountSerializer, RegisterSerializer, ProfileSerializer


User = get_user_model()

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    user = None

    def perform_create(self, serializer):
        self.user = serializer.save()

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)

        payload = jwt_payload_handler(self.user)
        return Response({'token': jwt_encode_handler(payload)}, status=status.HTTP_201_CREATED)


class MyProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.none()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user
