from reactbackapp.models import MyUser
from reactbackapp.models import Product, Operation
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    avatar_url = serializers.SerializerMethodField(read_only=True)
    avatar = serializers.ImageField(write_only=True)

    def get_avatar_url(self, obj):
        absolute = self.context['request'].build_absolute_uri()
        schema = absolute.split('//')[0][:-1]
        return "{}://{}/{}".format(schema, self.context['request'].get_host(), obj.avatar.url)

    class Meta:
        model = MyUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'avatar', 'avatar_url', 'password']

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
    image_url = serializers.SerializerMethodField('get_image')

    def get_image(self, obj):
        absolute = self.context['request'].build_absolute_uri()
        schema = absolute.split('//')[0][:-1]
        return "{}://{}/{}".format(schema, self.context['request'].get_host(), obj.image.url)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image_url']


class OperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operation
        fields = ['id', 'type', 'description', 'quantity', 'operation_product', 'operation_user', 'created_at']