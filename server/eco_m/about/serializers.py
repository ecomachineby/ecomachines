from rest_framework import serializers

from about.models import HelpText, Step, About
from api.utils import get_url_file


class HelpTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpText
        fields = [
            "id",
            "category",
            "text",
        ]


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = [
            "id",
            "title",
            "image",
            "description",
        ]

    def get_image(self, obj):
        return get_url_file(
            field=obj.image,
            request=self.context.get('request')
        )


class AboutSerializer(serializers.ModelSerializer):
    steps = StepSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = About
        fields = [
            "id",
            "slogan",
            "steps",
        ]

