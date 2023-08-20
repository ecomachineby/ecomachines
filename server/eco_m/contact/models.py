from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Social(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=120,
    )
    link = models.URLField(
        verbose_name=_("Link"),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Social')
        verbose_name_plural = _('Socials')


class DetailInfo(models.Model):
    title = models.TextField(
        verbose_name=_("Title"),
    )
    value = models.TextField(
        verbose_name=_("Value"),
        default="['', ]",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Detail Info')
        verbose_name_plural = _('Detail Info')


class Contact(models.Model):
    office_phone = models.CharField(
        verbose_name=_("Office phone"),
        max_length=50,
        validators=[
            RegexValidator(
                regex=r"^\+\d{3}[\s\S]*\d{2}[\s\S]*\d{3}[\s\S]*\d{2}[\s\S]*\d{2}$",
                message="Phone number must be in the format: '+999999999999'.",
            )
        ],
    )
    corporate_email = models.CharField(
        verbose_name=_("Corporate email"),
        max_length=255,
    )
    messanger = models.ManyToManyField(
        Social,
        verbose_name=_("Messanger"),
        blank=True,
    )
    detail_info = models.ManyToManyField(
        DetailInfo,
        verbose_name=_("Detail info"),
        blank=True,
    )
    partner_email = models.CharField(
        verbose_name=_("Partner email"),
        max_length=255,

    )
    vacancy_email = models.CharField(
        verbose_name=_("Vacancy email"),
        max_length=255,

    )
    primal_address = models.CharField(
        verbose_name=_("Primal address"),
        max_length=255,
    )
    context_footer = models.CharField(
        verbose_name=_("ContextFooter"),
        max_length=255,
    )
    coordinate_x = models.CharField(
        verbose_name=_("Coordinate X"),
        max_length=255,
    )
    coordinate_y = models.CharField(
        verbose_name=_("Coordinate Y"),
        max_length=255,
    )

    def __str__(self):
        return self.corporate_email

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
