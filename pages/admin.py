
# Register your models here.
from django.contrib import admin
from .models import Contact, SEOScoreSubscription, NewsletterSubscription

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'website')

@admin.register(SEOScoreSubscription)
class SEOScoreSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('website', 'email')

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email',)
