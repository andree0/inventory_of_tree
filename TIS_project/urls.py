"""TIS_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import django.contrib.auth.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from TIS_app import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', v.IndexView.as_view(), name="index"),
    path('register/', v.RegisterView.as_view(), name="register"),
    path('inventory/create/', v.CreateNewInventoryView.as_view(),
         name="create_inventory"),
    path('inventory/all/', v.AllInventoryView.as_view(),
         name="all_inventory"),
    # path('accounts/', include('allauth.urls')),

    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')),
    path('api/inventory/all/', v.AllInventoryAPIView.as_view(),
         name='api_inventory_all'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT
                          )
