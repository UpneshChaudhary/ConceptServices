from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_form, name='contact_form'),
    path('subscribe/', views.seo_subscription, name='seo_subscription'),
    path('newsletter/', views.newsletter_subscription, name='newsletter_subscription'),
    path('success/', views.success, name='success'),  # Success page after form submission
    

]