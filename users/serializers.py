from rest_framework import serializers
from django.contrib.auth.models import User
import random
import string

from users.models import UserConfirmation


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False
        )
        UserConfirmation.objects.create(
            user=user,
            confirmation_code=''.join(random.choices(string.digits, k=6))
        )
        return user

class UserConfirmationSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user_confirmation = UserConfirmation.objects.get(user__username=data['username'],
                                                             confirmation_code=data['confirmation_code'])
        except UserConfirmation.DoesNotExist:
            raise serializers.ValidationError("Invalid confirmation code")
        return data

    def save(self, validated_data):
        user_confirmation = UserConfirmation.objects.get(user__username=validated_data['username'])
        user_confirmation.user.is_active = True
        user_confirmation.user.save()
        user_confirmation.delete()
        return user_confirmation.user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
