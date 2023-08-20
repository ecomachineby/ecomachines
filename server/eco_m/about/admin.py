from django.contrib import admin
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from about.models import HelpText, Step, About


@admin.action(description="Perform duplicate")
def create_duplicate(self, request, queryset):
    for obj in queryset:
        obj.pk = None  # Set the primary key to None to create a new instance
        obj.save()


@admin.register(HelpText)
class HelpTextAdmin(admin.ModelAdmin):
    list_display = [
        "category",
        "text",
    ]
    actions = [create_duplicate, ]


class HelpTextWagAdmin(ModelAdmin):
    model = HelpText
    menu_label = 'HelpText'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "category",
        "text",
    ]


modeladmin_register(HelpTextWagAdmin)


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
    ]
    actions = [create_duplicate, ]


class StepWagAdmin(ModelAdmin):
    model = Step
    menu_label = 'Step'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "title",
        "description",
    ]


modeladmin_register(StepWagAdmin)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = [
        "slogan",
    ]
    filter_horizontal = ["steps"]
    actions = [create_duplicate, ]


class AboutWagAdmin(ModelAdmin):
    model = About
    menu_label = 'About'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "slogan",
    ]
    filter_horizontal = ["steps"]


modeladmin_register(AboutWagAdmin)

