from .models import User, Likes
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .utils import distance_users


class UsersRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            gender=validated_data['gender'],
            image=validated_data['image'],
        )
        return user

    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email", "gender", "image")


class UsersListSerializer(serializers.ModelSerializer):
    dist = serializers.SerializerMethodField()

    class Meta:
        fields = ('first_name', 'last_name', 'gender', 'dist')
        model = User

    def get_dist(self, instance):
        current_user = self.context['request'].user
        return distance_users(current_user.longitude, current_user.latitude, instance.longitude, instance.latitude)


class MatchSerializer(serializers.ModelSerializer):
    initiator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        if data['recipient'] == data['initiator']:
            raise serializers.ValidationError('Ошибка, нельзя ставить лайк самому себе')
        return data

    class Meta:
        model = Likes
        fields = ('initiator', 'recipient')

    validators = [
        UniqueTogetherValidator(queryset=Likes.objects.all(), fields=['initiator', 'recipient'],
                                message='Вы уже поставили лайк')]
