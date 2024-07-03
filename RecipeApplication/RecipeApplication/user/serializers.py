from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
	def create(self, validated_data):
		user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
		return user
	
	class Meta:
		model = User
		fields = '__all__'
