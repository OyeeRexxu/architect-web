from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(max_length=50, help_text="Icon class name (e.g., 'calculator')")
    image = models.CharField(max_length=200, blank=True, help_text="Path to service image (e.g., 'services/estimation.png')")
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
        # Return items from the first section of type 'list'
        section = self.sections.filter(section_type='list').first()
        if section:
            return section.get_items_list()[:5]
        return []

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
    items = models.TextField(blank=True, help_text="Enter items separated by newlines (for Lists/Process/Benefits)")
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
    image = models.CharField(max_length=200, help_text="Path to image (e.g., 'services/gallery/1.jpg')")
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image for {self.service.title}"

class ServiceSoftware(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='software')
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=200, help_text="Path to logo (e.g., 'software/autocad.png')")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Service Software"

    def __str__(self):
        return f"{self.name} ({self.service.title})"
