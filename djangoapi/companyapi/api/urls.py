from django.urls import path, include  # Include 'include' for router.urls
from rest_framework import routers
from .views import CompanyViewSet, EmployeeViewSet

# Define the router and register the viewsets
router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)

# Define the urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Properly include router.urls
]