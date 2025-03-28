from django.contrib import admin
from .models import Offer

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'type',
        'section',
        'category',
        'instrument',
        'style',
        'city',
        'created_on',
        'author',
        'filled',
    )
    list_filter = (
        'type',
        'section',
        'category',
        'instrument',
        'style',
        'filled',
        'created_on',
    )
    search_fields = (
        'title',
        'summary',
        'description',
        'instrument',
        'style',
        'city',
        'contact_name',
        'contact_email',
        'author__username',
    )
    ordering = ('-created_on',)
    readonly_fields = ('created_on',)

    fieldsets = (
        ('Informations générales', {
            'fields': ('type', 'section', 'category', 'title', 'summary', 'description')
        }),
        ('Tags & localisation', {
            'fields': ('instrument', 'style', 'city')
        }),
        ('Contact', {
            'fields': (
                'contact_name',
                'contact_email',
                'contact_phone',
                'contact_website',
                'contact_details',
                'show_author_mail',
            )
        }),
        ('Statut & auteur', {
            'fields': ('filled', 'author', 'created_on', 'moderation')
        }),
    )
