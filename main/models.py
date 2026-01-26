from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(max_length=50, help_text="Icon class name (e.g., 'calculator')")
    image = models.ImageField(upload_to='services/', blank=True, help_text="Path to service image (e.g., 'services/estimation.png')")
    overview = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_preview_items(self):
        # Return first 5 feature titles for preview
        return [f.title for f in self.features.all()[:5]]

    class Meta:
        ordering = ['order']

class ServiceSection(models.Model):
    SECTION_TYPES = (
        ('text', 'Text Block'),
        ('list', 'List (Bullet Points)'),
        ('process', 'Process Steps'),
        ('benefits', 'Benefits (Checkmarks)'),
        ('tags', 'Tags (Who Can Benefit)'),
    )

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='sections')
    heading = models.CharField(max_length=200, blank=True)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, default='text')
    content = models.TextField(blank=True, help_text="Main text content")
    items = models.TextField(blank=True, help_text="List items separated by newlines")
    is_subsection = models.BooleanField(default=False, help_text="If True, this section will be rendered as a sub-section of the previous block (e.g., inside Overview)")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_items_list(self):
        if not self.items:
            return []
        return [item.strip() for item in self.items.split('\n') if item.strip()]

    def __str__(self):
        return f"{self.service.title} - {self.heading}"

class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='services/gallery/', help_text="Path to image (e.g., 'services/gallery/1.jpg')")
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image for {self.service.title}"



class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="FontAwesome class (e.g., 'fa-solid fa-check')")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

# ==========================================
# CMS MODELS
# ==========================================

class SingletonModel(models.Model):
    """Abstract class for Singleton models (only one instance allowed)"""
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class SiteSettings(SingletonModel):
    site_name = models.CharField(max_length=100, default="ConstructPro")
    logo = models.ImageField(upload_to='site_logos/', blank=True, null=True, help_text="Upload logo image")
    phone_number = models.CharField(max_length=20, default="+1 123 456 7895")
    email = models.EmailField(default="info@constructorpro.com")
    address = models.TextField(default="1234 Builder Lane, Architect City, AC 54321")
    show_address = models.BooleanField(default=True, help_text="Toggle to show/hide address on the site")
    footer_description = models.TextField(blank=True, default="Building with Nature's Wisdom")
    
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Site Settings (Global)"

    def __str__(self):
        return "Site Settings"

class HomePage(SingletonModel):
    # Hero Section
    hero_title = models.CharField(max_length=200, default="Building with Nature's Wisdom")
    hero_subtitle = models.TextField(blank=True, default="Thoughtful construction advancing the balance between sustainability and architectural global innovation.")
    hero_bg_image = models.ImageField(upload_to='hero_images/', blank=True, null=True, help_text="Upload a hero background image")
    
    # About Section
    about_heading = models.CharField(max_length=200, default="Building Global Partnerships")
    about_content = models.TextField(blank=True, help_text="HTML allowed")
    
    # Services Header
    services_subtitle = models.CharField(max_length=100, default="Our Services")
    services_heading = models.CharField(max_length=200, default="Comprehensive Solutions for Every Project")
    services_description = models.TextField(blank=True, default="From CAD drafting to interior design, we deliver expert services tailored to your construction and architectural needs.")
    services_bg_image = models.ImageField(upload_to='images/', default="images/services_header_bg.png")
    
    # Software Section
    software_label = models.CharField(max_length=50, default="Toolset")
    software_heading = models.CharField(max_length=200, default="Technical Precision")
    software_description = models.TextField(blank=True, default="Our software stack ensures millimeter-perfect execution.")
    
    # Free Sample Section
    free_sample_heading = models.CharField(max_length=200, default="Get a Free Sample")
    free_sample_description = models.TextField(blank=True, default="Send us your drawings (PDF/DWG) and receive a complimentary sample to evaluate our quality and accuracy.")

    class Meta:
        verbose_name_plural = "Home Page Content"

    def __str__(self):
        return "Home Page Content"

class AboutPage(SingletonModel):
    # Deck Section
    deck_subtitle = models.CharField(max_length=100, default="ABOUT US")
    deck_heading = models.CharField(max_length=200, default="Building Global Partnerships")
    deck_content_1 = models.TextField(blank=True)
    deck_content_2 = models.TextField(blank=True)
    
    # Vision & Mission
    vision_heading = models.CharField(max_length=200, default="Shaping the Future Together")
    vision_content = models.TextField(blank=True)
    mission_heading = models.CharField(max_length=200, default="Delivering Excellence in Every Project")
    mission_content = models.TextField(blank=True)
    
    # Stats
    stat_1_value = models.CharField(max_length=50, default="20+")
    stat_1_label = models.CharField(max_length=100, default="Years of Excellence")
    stat_2_value = models.CharField(max_length=50, default="11.5K")
    stat_2_label = models.CharField(max_length=100, default="Projects Completed")

    class Meta:
        verbose_name_plural = "About Page Content"

    def __str__(self):
        return "About Page Content"

class ContactPage(SingletonModel):
    # Visual Side
    visual_badge = models.CharField(max_length=50, default="EST. 2005")
    visual_heading = models.CharField(max_length=200, default="Design your legacy.")
    visual_image = models.ImageField(upload_to='contact_visuals/', default='contact_visuals/contact_illustration.png')
    
    # Form Side
    form_subtitle = models.CharField(max_length=100, default="Get in Touch")
    form_heading = models.CharField(max_length=200, default="Start the Conversation")
    form_description = models.TextField(blank=True, default="Ready to bring your vision to life? Our team of architects and engineers is here to help you every step of the way.")
    
    # Response Time
    response_title = models.CharField(max_length=200, default="24-Hour Response Guarantee")
    response_description = models.TextField(blank=True, default="We typically respond within 24 hours. Most projects have a 24-48 hour turnaround time.")

    class Meta:
        verbose_name_plural = "Contact Page Content"

    def __str__(self):
        return "Contact Page Content"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default="Customer")
    content = models.TextField()
    rating = models.IntegerField(default=5)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.role}"

class SoftwareTool(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/software/', help_text="Path to logo image")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class WhyChooseUsItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_svg = models.TextField(help_text="Paste SVG path or full SVG code here")
    order = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Why Choose Us Items"
        ordering = ['order']

    def __str__(self):
        return self.title

class CommitmentItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    number = models.CharField(max_length=10, default="01")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class AboutGalleryImage(models.Model):
    """Images for the About Us card deck"""
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about_gallery/')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class ProcessStep(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    number = models.CharField(max_length=10, default="01")
    icon_svg = models.TextField(help_text="Paste SVG path or full SVG code here")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=50, choices=[
        ('project', 'New Project Inquiry'),
        ('career', 'Careers'),
        ('other', 'Other')
    ], blank=True)
    message = models.TextField()
    file = models.FileField(upload_to='contact_uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

