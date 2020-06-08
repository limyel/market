from rest_framework import serializers

from .models import VerifyCode, User


class VerifyCodeSerializer(serializers.Serializer):

    code = serializers.CharField(max_length=4, required=True)
    phone = serializers.CharField(max_length=11, required=True)

    def create(self, validated_data):
        return VerifyCode.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=64, required=True)
    phone = serializers.CharField(max_length=11, required=True)
    picture = serializers.ImageField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.save()
        return instance
