from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name','email', 'phone', 'address', 'city', 'state', 'bio', 'linkedin','instagram']