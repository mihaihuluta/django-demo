from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from apps.accounts import views


urlpatterns = [
    url(r'auth/$', obtain_jwt_token, name='obtain_token'),
    url(r'auth/refresh_token/$', refresh_jwt_token, name='refresh_token'),
    url(r'auth/verify_token/$', verify_jwt_token, name='verify_token'),

    url(r'register/$', views.RegisterView.as_view(), name='register'),
]
