from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, \
    IsAuthenticated, SAFE_METHODS

from .serializers import ReviewSerializer
from .models import Review
from .permissions import IsOwnerOrReadOnly


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = ReviewSerializer

    def get_queryset(self):
        user = self.request.user
        return Review.objects.filter(user=user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
