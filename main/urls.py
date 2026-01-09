from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new-home/', views.new_home, name='new_home'),
    path('about/', views.about, name='about'),
    path('design-variants/', views.design_variants, name='design_variants'),
    path('service-variants/', views.service_variants, name='service_variants'),
    path('service-variants-animated/', views.service_variants_animated, name='service_variants_animated'),
    path('demo-service/', views.demo_service, name='demo_service'),
    path('service-detail-variants/', views.service_detail_variants, name='service_detail_variants'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
    path('footer-variants/', views.footer_variants, name='footer_variants'),
    path('contact/', views.contact, name='contact'),
    path('hero-variants/', TemplateView.as_view(template_name='hero_variants.html'), name='hero_variants'),
    path('service-header-variants/', TemplateView.as_view(template_name='service_header_variants.html'), name='service_header_variants'),
    path('software-variants/', TemplateView.as_view(template_name='software_variants.html'), name='software_variants'),
    path('about-intro-variants/', TemplateView.as_view(template_name='about_intro_variants.html'), name='about_intro_variants'),
    path('backup/', views.backup_files, name='backup_files'),
    path('vertical-slice-variants/', TemplateView.as_view(template_name='vertical_slice_variants.html'), name='vertical_slice_variants'),
]
