from django.contrib import admin

from main.models import Contact, Slider


@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display = [
        'title',
        'admin_image',
        'is_active',
    ]
    list_per_page = 20
    list_editable = [
        'is_active',
    ]


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = [
        'name',
        'phone',
        'text',
        'pub_date',
    ]
    list_per_page = 20

