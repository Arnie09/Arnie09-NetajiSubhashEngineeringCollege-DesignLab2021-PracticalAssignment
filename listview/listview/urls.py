"""listview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from list.views import add_data, delete_data, delete_all, list_items, index, select_items, show_selected

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_data/', add_data, name="add_data"),
    path('delete_items/', delete_data, name="delete_data"),
    path('delete_data/', delete_all, name="delete_all_data"),
    path('list/', list_items, name="list_data"),
    path('', index, name="index"),
    path('select_items/', select_items, name="select_items"),
    path('show_selected/', show_selected, name="show_selected")
]
