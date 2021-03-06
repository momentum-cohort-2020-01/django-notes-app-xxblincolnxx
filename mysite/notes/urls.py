"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from core import views

urlpatterns = [
    path('', views.notes_list, name ='notes_list'),
    path('notes/<int:pk>', views.notes_detail, name='notes_detail'),
    path('new_note/', views.new_note, name = 'new_note'),
    path('notes/<int:pk>/edit/', views.edit_note, name = 'edit_note'),
    path('notes/<int:pk>/remove/', views.remove_note, name='remove_note'),
    path('admin/', admin.site.urls),
]
