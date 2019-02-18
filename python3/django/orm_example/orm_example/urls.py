"""orm_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from orm_example import views, models

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('person/', views.people, name='person-list'),
    path('person/detail/<int:pk>', models.PersonDetail.as_view(), name='person-detail'),
    path('person/edit/<int:pk>', models.PersonUpdate.as_view(), name='person-update'),
    path('person/delete/<int:pk>', models.PersonDelete.as_view(), name='person-delete'),
]
