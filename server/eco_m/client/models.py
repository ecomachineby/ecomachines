from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from product.models import Product


class ProductFile(models.Model):
    profile = models.ForeignKey(
        "Client",
        related_name="product_file",
        verbose_name=_("Profile"),
        on_delete=models.CASCADE,
    )
    client_product = models.ForeignKey(
        "ClientProduct",
        verbose_name=_("Client Product"),
        related_name="files",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    date = models.DateField(
        verbose_name=_("Date"),
        default=timezone.now,
    )
    file = models.FileField(
        verbose_name=_("File"),
    )

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = _("Product File")
        verbose_name_plural = _("Product Files")


class ClientProduct(models.Model):
    code = models.CharField(
        verbose_name=_("Code"),
        max_length=120,
    )
    profile = models.ForeignKey(
        "Client",
        related_name="products",
        verbose_name=_("Profile"),
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        related_name="products",
        on_delete=models.CASCADE,
    )
    date = models.DateField(
        verbose_name=_("Date"),
        default=timezone.now,
    )

    def __str__(self):
        return f"{self.product}-{self.code}"

    class Meta:
        verbose_name = _("Client Product")
        verbose_name_plural = _("Client Products")


class Comment(models.Model):
    profile = models.ForeignKey(
        "Client",
        verbose_name=_("Profile"),
        related_name="comments",
        on_delete=models.CASCADE,
    )
    value = models.PositiveIntegerField(
        verbose_name=_("Value")
    )
    text = models.TextField(
        verbose_name=_("Text"),
        blank=True,
    )
    date = models.DateField(
        verbose_name=_("Date"),
        default=timezone.now,
    )

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class Client(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    title_object = models.CharField(
        verbose_name=_("Title object"),
        help_text="Наименование объекта",
        max_length=120,
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        help_text="Изображение объекта",

    )
    company = models.CharField(
        verbose_name=_("Company"),
        max_length=255,
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")
