from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class Authentication(ModelBackend):
    def authenticate(self, username=None, email=None, password=None):
        email = email or username
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(
                Q(email__iexact=email)
            )
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user.
            UserModel().set_password(password)
        return None
