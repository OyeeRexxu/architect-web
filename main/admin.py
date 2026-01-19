from django.contrib import admin
from .models import (
    Service, ServiceSection, ServiceImage, ServiceFeature,
    SiteSettings, HomePage, AboutPage, ContactPage,
    Testimonial, SoftwareTool, WhyChooseUsItem, CommitmentItem, AboutGalleryImage,
    ProcessStep
)

# Register your models here.

class SingletonModelAdmin(admin.ModelAdmin):
    """Prevents adding new instances if one exists"""
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

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

@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
    fieldsets = (
        ('General', {'fields': ('site_name', 'logo', 'footer_description')}),
        ('Contact Info', {'fields': ('phone_number', 'email', 'address')}),
        ('Social Media', {'fields': ('facebook_url', 'twitter_url', 'linkedin_url', 'instagram_url')}),
    )

@admin.register(HomePage)
class HomePageAdmin(SingletonModelAdmin):
    fieldsets = (
        ('Hero Section', {'fields': ('hero_title', 'hero_subtitle', 'hero_bg_image')}),
        ('About Section', {'fields': ('about_heading', 'about_content')}),
        ('Services Header', {'fields': ('services_heading', 'services_subtitle', 'services_description', 'services_bg_image')}),
        ('Software Header', {'fields': ('software_label', 'software_heading', 'software_description')}),
        ('Free Sample', {'fields': ('free_sample_heading', 'free_sample_description')}),
    )

@admin.register(AboutPage)
class AboutPageAdmin(SingletonModelAdmin):
    fieldsets = (
        ('Deck Section', {'fields': ('deck_subtitle', 'deck_heading', 'deck_content_1', 'deck_content_2')}),
        ('Vision', {'fields': ('vision_heading', 'vision_content')}),
        ('Mission', {'fields': ('mission_heading', 'mission_content')}),
        ('Stats', {'fields': ('stat_1_value', 'stat_1_label', 'stat_2_value', 'stat_2_label')}),
    )

@admin.register(ContactPage)
class ContactPageAdmin(SingletonModelAdmin):
    fieldsets = (
        ('Visual Section', {'fields': ('visual_badge', 'visual_heading', 'visual_image')}),
        ('Form Section', {'fields': ('form_subtitle', 'form_heading', 'form_description')}),
        ('Response Guarantee', {'fields': ('response_title', 'response_description')}),
    )

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'content')

@admin.register(SoftwareTool)
class SoftwareToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'order')
    list_editable = ('order',)

@admin.register(WhyChooseUsItem)
class WhyChooseUsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(CommitmentItem)
class CommitmentItemAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'order')
    list_editable = ('order',)

@admin.register(AboutGalleryImage)
class AboutGalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'order')
    list_editable = ('order',)

@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'order')
    list_editable = ('order',)
