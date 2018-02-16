from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from apps.reviews.views import ReviewViewSet

router = SimpleRouter()
router.register(r'', ReviewViewSet)

urlpatterns = [
]

urlpatterns += router.urls
