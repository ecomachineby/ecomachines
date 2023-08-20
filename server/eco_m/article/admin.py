from django.contrib import admin
from wagtail.contrib.modeladmin.options import modeladmin_register, ModelAdmin

from about.admin import create_duplicate
from article.models import Article


@admin.register(Article)
class AboutAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "image",
    ]
    actions = [create_duplicate, ]


class AboutWagAdmin(ModelAdmin):
    model = Article
    menu_label = 'Article'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "title",
        "image",
    ]


modeladmin_register(AboutWagAdmin)
