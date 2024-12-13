from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('about_us', views.about, name='About'),
    path('equipment', views.eq, name='Eq'),
    path('pricing', views.pricing, name='Pricing'),
    path('FAQs', views.faqs, name='FAQ')
]
