from django.urls import path
from .views import ProfileDetail,all_profiles

urlpatterns = [
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('profiles/', all_profiles.as_view(),name='all-profile'),
]
