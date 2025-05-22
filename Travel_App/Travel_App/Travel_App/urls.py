"""
URL configuration for Travel_App project.

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
from django.conf import settings
from django.conf.urls.static import static
from Travel_Application.views import index, add_travel, edit_travel, delete_travel, contact, details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('add-travel/', add_travel, name='add-travel'),
    path('edit-travel/<int:travel_id>/', edit_travel, name='edit-travel'),
    path('delete-travel/<int:travel_id>/', delete_travel, name='delete-travel'),
    path('contact/', contact, name='contact'),
    path('details/<travel_id>', details, name='details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
