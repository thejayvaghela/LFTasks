from rest_framework import serializers
from .models import CustomUser,CustomManager

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=('mobileNo','first_name','last_name','address','password')
        # extra_kwargs = {'password': {'write_only': True}}
        
        def create(self, serialized_data):
            user = CustomManager.objects.create_user(serialized_data['mobileNo'], serialized_data['first_name'], serialized_data['password'])
            return user