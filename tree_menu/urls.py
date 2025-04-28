from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='tree_menu/home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='tree_menu/about.html'), name='about'),
    path('services/', TemplateView.as_view(template_name='tree_menu/services.html'), name='services'),
    path('services/web/', TemplateView.as_view(template_name='tree_menu/web_services.html'), name='web_services'),
    path('services/mobile/', TemplateView.as_view(template_name='tree_menu/mobile_services.html'), name='mobile_services'),
    path('contact/', TemplateView.as_view(template_name='tree_menu/contact.html'), name='contact'),
]