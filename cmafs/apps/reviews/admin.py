from django.contrib import admin

from . import models


class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = (
    )

    list_display = (
        'title',
        'summary',
        'ip_address',
        'submission_date',
        'user',
        'company',
        'rating',
    )

    search_fields = (
        'title',
        'summary'
    )


admin.site.register(models.Review, ReviewAdmin)
