from django.db import models
from django.utils.translation import gettext_lazy as _


class HelpText(models.Model):
    category = models.CharField(
        verbose_name=_("Category"),
        max_length=100,
    )
    text = models.TextField(
        verbose_name=_("Text"),
    )

    def __str__(self):
        return self.category

    class Meta:
        ordering = [
            "category",
        ]
        verbose_name = _("Help Text")
        verbose_name_plural = _("Help Texts")


class Step(models.Model):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=120,
    )
    image = models.ImageField(
        verbose_name=_("Image"),
    )
    description = models.TextField(
        verbose_name=_("Description"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Step")
        verbose_name_plural = _("Steps")


class About(models.Model):
    slogan = models.CharField(
        verbose_name=_("Slogan"),
        max_length=255,
    )
    steps = models.ManyToManyField(
        Step,
        verbose_name=_("Steps"),
        related_name='abouts',
        blank=True,
    )

    def __str__(self):
        return self.slogan

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
