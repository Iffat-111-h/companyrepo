from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),  # Home page
    path('api/v1/', include('api.urls')),  # Include API URLs
]
