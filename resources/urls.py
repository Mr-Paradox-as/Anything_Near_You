from django.urls import path
from .views import all_resources,resources_detail

urlpatterns = [
    path('details/<int:pk>/', resources_detail.as_view(), name='resource-detail'),
    path('all', all_resources.as_view(),name='all-resources'),
]
