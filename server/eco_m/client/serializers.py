from api.utils import get_url_file
from product.models import Product
from .models import (
    Client,
    ProductFile,
    Comment,
    ClientProduct,
)
from rest_framework import serializers


class ProductFileSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d.%m.%Y")
    file = serializers.SerializerMethodField()

    class Meta:
        model = ProductFile
        fields = [
            "id",
            "date",
            "file",
        ]

    def get_file(self, obj):
        return get_url_file(
            field=obj.file,
            request=self.context.get('request')
        )


class CommentSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(required=True)
    text = serializers.CharField(required=False)

    class Meta:
        model = Comment
        fields = [
            "text",
            "value",
            "profile",
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    message = serializers.CharField(required=True)
    value = serializers.IntegerField(required=True)
    text = serializers.CharField(required=False)

    class Meta:
        model = Comment
        fields = [
            "text",
            "value",
            "message",
        ]

    def create(self, validated_data):
        value_str = validated_data.get("value", None)
        text = validated_data.get("text", None)
        profile = validated_data.get("profile", None)

        value = int(value_str)
        user = Comment.objects.create(
            profile=profile,
            value=value,
            text=text,
        )

        return user


class ClientProductProductSerializer(serializers.ModelSerializer):
    front_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "title",
            "slug",
            "front_image",
        ]

    def get_front_image(self, obj):
        return get_url_file(
            field=obj.front_image,
            request=self.context.get('request')
        )


class ClientProductSerializer(serializers.ModelSerializer):
    product = ClientProductProductSerializer(many=False)
    files = ProductFileSerializer(many=True)
    date = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = ClientProduct
        fields = [
            "product",
            "date",
            "files",
            "code",
        ]


class ClientSerializer(serializers.ModelSerializer):
    products = ClientProductSerializer(many=True)

    class Meta:
        model = Client
        fields = [
            "id",
            "user",
            "title_object",
            "image",
            "company",
            "products",
        ]
