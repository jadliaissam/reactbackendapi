from reactbackapp.models import MyUser
from reactbackapp.models import Product, Operation
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'avatar', 'password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image']


class OperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operation
        fields = ['id', 'type', 'description', 'quantity', 'operation_product', 'operation_user', 'created_at']