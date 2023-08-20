from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    modeladmin_register, ModelAdmin
)

from about.admin import create_duplicate
from product.models import (
    Product,
    ProductImage
)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [
        "image",
    ]
    search_fields = ["image"]
    actions = [create_duplicate, ]


class ProductImageWagAdmin(ModelAdmin):
    model = ProductImage
    menu_label = 'ProductImage'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "image",
    ]
    search_fields = ["image"]


modeladmin_register(ProductImageWagAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "date",
        "published"
    ]

    list_filter = [
        "date",
        "published",
    ]
    filter_horizontal = [
        "images"
    ]
    search_fields = ["title", ]
    actions = [create_duplicate, ]


class ProductWagAdmin(ModelAdmin):
    model = Product
    menu_label = 'Product'
    menu_icon = 'doc-full-inverse'
    list_display = [
        "title",
        "date",
        "published"
    ]

    list_filter = [
        "date",
        "published",
    ]
    filter_horizontal = [
        "images"
    ]
    search_fields = ["title", ]


modeladmin_register(ProductWagAdmin)
