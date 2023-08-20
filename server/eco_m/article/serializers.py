from rest_framework import serializers
from wagtail.templatetags.wagtailcore_tags import richtext

from api.utils import get_url_file
from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "image",
            "text",
        ]

    def get_text(self, obj):
        return richtext(obj.text)

    def get_image(self, obj):
        return get_url_file(
            field=obj.image,
            request=self.context.get('request')
        )
