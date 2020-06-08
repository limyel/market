from rest_framework import serializers

from goods.serializer import GoodsSerializer
from goods.models import Good
from .models import Favorite, Address


class FavoritesSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    good = serializers.PrimaryKeyRelatedField(required=True, queryset=Good.objects.all())
    # good = GoodsSerializer(read_only=True)

    def create(self, validated_data):
        self.user = self.context['request'].user
        self.good = validated_data['good']
        favorite = Favorite.objects.create(user=self.user, good=self.good)
        return favorite

    def update(self, instance, validated_data):
        return super(serializers.Serializer, self).update(instance, validated_data)

    # class Meta:
    #     model = Favorite
    #     fields = ['id', 'user', 'good']


class AddressSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Address
        fields = '__all__'
