from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new-home/', views.new_home, name='new_home'),
    path('about/', views.about, name='about'),
    path('design-variants/', views.design_variants, name='design_variants'),
    path('service-variants/', views.service_variants, name='service_variants'),
    path('service-variants-animated/', views.service_variants_animated, name='service_variants_animated'),
    path('service-detail-variants/', views.service_detail_variants, name='service_detail_variants'),
    path('service/<slug:slug>/', views.service_detail, name='service_detail'),
    path('footer-variants/', views.footer_variants, name='footer_variants'),
    path('contact/', views.contact, name='contact'),
]
