from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError



UserModel = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = UserModel
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'birth_year')


    def create(self, validated_data):
        del validated_data['password2']

        user = UserModel.objects.create_user(
            **validated_data
        )

        return user


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError('Password must same')

        return attrs
