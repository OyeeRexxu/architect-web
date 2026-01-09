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
    image = models.CharField(max_length=200, help_text="Path to image (e.g., 'services/gallery/1.jpg')")
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
