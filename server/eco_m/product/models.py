from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductImage(models.Model):
    image = models.ImageField(
        verbose_name=_("Image"),
    )

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = _("ProductImage")
        verbose_name_plural = _("ProductImages")


class Product(models.Model):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=120,
    )
    published = models.BooleanField(
        verbose_name=_("Published"),
        default=False,
    )
    slug = models.CharField(
        verbose_name=_("Slug"),
        max_length=120,
    )
    description = models.TextField(
        verbose_name=_("Content"),
        default="['', ]",
    )
    how_it_works = models.TextField(
        verbose_name=_("How it works"),
        default="['', ]",
    )
    specification = models.TextField(
        verbose_name=_("Characteristics"),
        default="['', ]",
    )
    images = models.ManyToManyField(
        ProductImage,
        verbose_name=_("Images"),
        blank=True,
    )
    front_image = models.FileField(
        verbose_name=_("Front image"),
    )
    pdf = models.FileField(
        verbose_name=_("PDF"),
    )
    date = models.DateField(
        verbose_name=_("Date"),
        default=timezone.now,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "-title",
            "-date",
        ]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
