from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django_countries.serializer_fields import CountryField

from rest_framework import serializers, exceptions

User = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.SlugField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    country = CountryField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'country')

    def validate_email(self, value):
        email = value.lower()

        if self.instance is not None:
            if User.objects.exclude(pk=self.instance.pk).filter(email__iexact=email).exists():
                raise ValidationError('A user with same email already exists!')

        return email

    def validate_username(self, value):
        username = value.lower()

        if self.instance is not None:
            if User.objects.exclude(pk=self.instance.pk).filter(username__iexact=username).exists():
                raise ValidationError('A user with same username already exists!')

        return username


class RegisterSerializer(AccountSerializer):
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        email = value.lower()

        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError('A user with same email already exists!')

        return email

    def validate_username(self, value):
        username = value.lower()

        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError('A user with same username already exists!')

        return username

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileSerializer(AccountSerializer):
    email = serializers.EmailField(required=False)
    country = CountryField(required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'country',
            'about_me',
        )
