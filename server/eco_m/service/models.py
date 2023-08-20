from django.db import models
from wagtail.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class Stage(models.Model):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=120,
    )
    description = models.TextField(
        verbose_name=_("Description"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Stage')
        verbose_name_plural = _('Stages')


class Service(models.Model):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=120,
    )
    best = models.BooleanField(
        verbose_name=_("Best"),
        default=False,
    )
    slug = models.CharField(
        verbose_name=_("Slug"),
        max_length=120,
    )
    image = models.ImageField(
        verbose_name=_("Image"),
    )
    description = models.TextField(
        verbose_name=_("Description"),
    )
    stages = models.ManyToManyField(
        Stage,
        verbose_name=_("Stages"),
        blank=True
    )
    constructor = RichTextField(
        verbose_name=_("Constructor"),
        blank=True,
        features=[
            "h1", "h2", "h3", "h4", "h5", "h6", "bold", "italic",
            "strikethrough", "blockquote", "ol", "ul", "hr", "link", "document-link",
            "image", "embed", "code", "superscript", "subscript",
        ]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
