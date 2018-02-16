from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

from apps.accounts.models import User


class Company(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=255)


class Review(models.Model):
    title = models.CharField(max_length=64)
    summary = models.TextField(max_length=10000)
    ip_address = models.GenericIPAddressField()
    submission_date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
