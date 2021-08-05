from django.urls import path
from home import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('glimpses/', views.glimpses, name='glimpses'),
    path('about-school/', views.about, name='about'),
    path('principal-message/', views.principal, name='principal'),
    path('administrator-message/', views.administrator, name='administrator'),
    path('president-message/', views.president, name='president'),
]
