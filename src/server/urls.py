"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='base.html'), name='about_page'),
    path('portfolio/', TemplateView.as_view(template_name='base.html'), name='portfolio'),
    path('portfolio/project-1/', TemplateView.as_view(template_name='base.html'), name='project_1'),
    path('portfolio/project-2/', TemplateView.as_view(template_name='base.html'), name='project_2'),
    path('contacts/', TemplateView.as_view(template_name='base.html'), name='contacts'),
    path('terms-of-service/', TemplateView.as_view(template_name='base.html'), name='terms-of-service'),
    path('privacy-policy/', TemplateView.as_view(template_name='base.html'), name='privacy_policy'),
]
