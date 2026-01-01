from django.contrib import admin
from .models import Service, ServiceSection, ServiceImage, ServiceSoftware

# Register your models here.

class ServiceSoftwareInline(admin.TabularInline):
    model = ServiceSoftware
    extra = 1

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

class ServiceSectionInline(admin.StackedInline):
    model = ServiceSection
    extra = 0
    fields = ('heading', 'section_type', 'content', 'items', 'order')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceSectionInline, ServiceImageInline, ServiceSoftwareInline]
    search_fields = ('title', 'overview')
    ordering = ('order',)
