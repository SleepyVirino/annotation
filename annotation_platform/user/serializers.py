from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'age', 'gender', 'email', 'phone_number', 'wechat_number',
                  'education_information')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            age=validated_data.get('age'),
            gender=validated_data.get('gender'),
            phone_number=validated_data.get('phone_number', ''),
            wechat_number=validated_data.get('wechat_number', ''),
            education_information=validated_data.get('education_information', '')
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'last_login', 'is_staff', 'age', 'gender', 'email', 'phone_number',
                  'wechat_number', 'education_information', 'created_at', 'updated_at')
        read_only_fields = ('id', 'username', 'last_login', 'is_staff', 'created_at', 'updated_at')
