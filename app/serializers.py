from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'




class Userserializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    def create(self,validated_data):
        user =User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


    class Meta:
        model=User
        fields=[
            'username',
            'password'
        ]
