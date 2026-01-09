from django.contrib import admin
from .models import Service, ServiceSection, ServiceImage, ServiceFeature

# Register your models here.

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1

class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

class ServiceSectionInline(admin.StackedInline):
    model = ServiceSection
    extra = 0
    fields = (('heading', 'section_type', 'order'), 'is_subsection', 'content', 'items')
    classes = ('collapse',)
    verbose_name = "Service Section / Sub-Service"
    verbose_name_plural = "Service Sections (Add Content Blocks Here)"

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceSectionInline, ServiceImageInline, ServiceFeatureInline]
    search_fields = ('title', 'overview')
    ordering = ('order',)
