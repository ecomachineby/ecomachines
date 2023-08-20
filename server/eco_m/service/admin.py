from django.contrib import admin
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from about.admin import create_duplicate
from service.models import Service, Stage


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = [
        "title",
    ]
    search_fields = ["title", ]
    actions = [create_duplicate, ]


class StageWagAdmin(ModelAdmin):
    model = Stage
    menu_label = 'Stage'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "title",
    ]
    search_fields = ["title", ]


modeladmin_register(StageWagAdmin)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "best",
    ]
    filter_horizontal = [
        "stages",
    ]
    search_fields = ["title", ]
    actions = [create_duplicate, ]


class ServiceWagAdmin(ModelAdmin):
    model = Service
    menu_label = 'Service'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "title",
        "best",
    ]
    filter_horizontal = [
        "stages",
    ]
    search_fields = ["title", ]


modeladmin_register(ServiceWagAdmin)
