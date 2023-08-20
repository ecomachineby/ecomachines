from rest_framework import serializers
from wagtail.templatetags.wagtailcore_tags import richtext

from service.models import Service, Stage


class StagesSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Stage
        fields = [
            "id",
            "title",
            "description",
        ]


class ServiceSerializer(serializers.ModelSerializer):
    stages = StagesSerializer(many=True)
    constructor = serializers.SerializerMethodField()

    def get_constructor(self, obj):
        return richtext(obj.constructor)

    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "best",
            "slug",
            "image",
            "description",
            "stages",
            "constructor",
        ]

