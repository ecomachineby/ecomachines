from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from about.admin import create_duplicate
from client.models import (
    Client,
    ProductFile,
    Comment,
    ClientProduct,
)


@admin.register(ClientProduct)
class ClientProductAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "code",
        "profile",
        "date",
    ]
    list_filter = [
        "profile",
        "product",
        "date",
    ]
    search_fields = [
        "code",
        "product",
    ]
    actions = [create_duplicate, ]


class ClientProductWagAdmin(ModelAdmin):
    model = ClientProduct
    menu_label = 'ClientProduct'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "product",
        "code",
        "profile",
        "date",
    ]
    list_filter = [
        "profile",
        "product",
        "date",
    ]
    search_fields = [
        "code",
        "product",
    ]


modeladmin_register(ClientProductWagAdmin)


@admin.register(ProductFile)
class ProductFileAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "client_product",
        "profile",
        "date",
    ]
    list_filter = [
        "date",
        "profile",
    ]
    search_fields = [
        "file",
    ]
    actions = [create_duplicate, ]


class ProductFileWagAdmin(ModelAdmin):
    model = ProductFile
    menu_label = 'ProductFile'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "__str__",
        "client_product",
        "profile",
        "date",
    ]
    list_filter = [
        "date",
        "profile",
    ]
    search_fields = [
        "file",
    ]


modeladmin_register(ProductFileWagAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "profile",
        "value",
        "text",
        "date",
    ]
    list_filter = [
        "profile",
        "value",
        "date",
    ]
    search_fields = [
        "value",
        "profile",
    ]
    actions = [create_duplicate, ]


class CommentWagAdmin(ModelAdmin):
    model = Comment
    menu_label = 'Comment'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "profile",
        "value",
        "text",
        "date",
    ]
    list_filter = [
        "profile",
        "value",
        "date",
    ]
    search_fields = [
        "value",
        "profile",
    ]


modeladmin_register(CommentWagAdmin)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "title_object",
        "image",
        "company",
    ]
    search_fields = [
        "user",
        "title_object"
    ]
    actions = [create_duplicate, ]


class ClientWagAdmin(ModelAdmin):
    model = Client
    menu_label = 'Client'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "user",
        "title_object",
        "image",
        "company",
    ]
    filter_horizontal = [
        "products",
        "comments",
    ]
    search_fields = [
        "user",
        "title_object"
    ]


modeladmin_register(ClientWagAdmin)
