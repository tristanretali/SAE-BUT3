from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    
	def create(self, validated_data):
		user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])
		group = Group.objects.get(name='Editors')
		user.groups.add(group)
		return user
	
	class Meta:
		model = User
		fields = '__all__'
