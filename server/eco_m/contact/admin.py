from django.contrib import admin
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from about.admin import create_duplicate
from contact.models import Social, Contact, DetailInfo


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "link",
    ]
    search_fields = ["name", "link"]


class SocialWagAdmin(ModelAdmin):
    model = Social
    menu_label = 'Social'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "name",
        "link",
    ]
    search_fields = ["name", "link"]


modeladmin_register(SocialWagAdmin)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "office_phone",
        "corporate_email",
        "partner_email",
        "primal_address",
    ]
    filter_horizontal = [
        "messanger",
    ]
    search_fields = [
        "office_phone",
        "corporate_email",
        "partner_email",
        "primal_address",
    ]
    actions = [create_duplicate, ]


class SocialWagAdmin(ModelAdmin):
    model = Contact
    menu_label = 'Contact'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "office_phone",
        "corporate_email",
        "partner_email",
        "primal_address",
    ]
    filter_horizontal = [
        "messanger",
    ]
    search_fields = [
        "office_phone",
        "corporate_email",
        "partner_email",
        "primal_address",
    ]


modeladmin_register(SocialWagAdmin)


@admin.register(DetailInfo)
class DetailInfoAdmin(admin.ModelAdmin):
    list_display = [
        "title"
    ]
    search_fields = [
        "title"
    ]
    actions = [create_duplicate, ]


class DetailInfoWagAdmin(ModelAdmin):
    model = DetailInfo
    menu_label = 'DetailInfo'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "title"
    ]
    search_fields = [
        "title"
    ]


modeladmin_register(DetailInfoWagAdmin)
