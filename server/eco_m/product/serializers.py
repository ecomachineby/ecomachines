import ast

from rest_framework import serializers

from api.utils import get_url_file
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    how_it_works = serializers.SerializerMethodField()
    specification = serializers.SerializerMethodField()
    front_image = serializers.SerializerMethodField()
    date = serializers.DateField(format="%d.%m.%Y")

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "how_it_works",
            "specification",
            "images",
            "pdf",
            "date",
            "front_image"
        ]

    def get_front_image(self, obj):
        return get_url_file(
            field=obj.front_image,
            request=self.context.get('request'),
        )

    def get_images(self, obj):
        images = obj.images.all()
        result = []
        for img in images:
            url = get_url_file(
                field=img.image,
                request=self.context.get('request')
            )
            result.append(url)
        return result

    def get_description(self, obj):
        return ast.literal_eval(obj.description)

    def get_how_it_works(self, obj):
        return ast.literal_eval(obj.how_it_works)

    def get_specification(self, obj):
        return ast.literal_eval(obj.specification)
