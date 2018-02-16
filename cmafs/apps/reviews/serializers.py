from rest_framework import serializers

from apps.reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'title', 'summary', 'ip_address', 'submission_date', 'user',
            'company', 'rating'
        )
        read_only_fields = ('user', 'submission_date')

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        return instance

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'name', 'description'
        )

    def save(self, **kwargs):
        instance = super().save(**kwargs)
        return instance
