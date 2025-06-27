from django.contrib import admin
from .models import NewsletterSubscriber

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'date_subscribed']
    search_fields = ['email']
    readonly_fields = ['date_subscribed']
    ordering = ['-date_subscribed']
