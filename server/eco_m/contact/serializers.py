import ast
from rest_framework import serializers
from contact.models import Contact, DetailInfo, Social


class SocialSerializer(serializers.ModelSerializer):
    link = serializers.URLField()

    class Meta:
        model = Social
        fields = [
            "id",
            "name",
            "link",
        ]


class DetailInfoSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    class Meta:
        model = DetailInfo
        fields = [
            "title",
            "value",
        ]

    def get_value(self, obj):
        return ast.literal_eval(obj.value)


class ContactSerializer(serializers.ModelSerializer):
    corporate_email = serializers.EmailField()
    messanger = SocialSerializer(many=True)
    detail_info = DetailInfoSerializer(many=True)
    partner_email = serializers.EmailField()
    vacancy_email = serializers.EmailField()

    class Meta:
        model = Contact
        fields = [
            "id",
            "office_phone",
            "corporate_email",
            "messanger",
            "detail_info",
            "partner_email",
            "vacancy_email",
            "primal_address",
            "context_footer",
            "coordinate_x",
            "coordinate_y",
        ]
