from django.db import models
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet
from django.utils.translation import gettext_lazy as _


@register_snippet
class Article(models.Model):
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=120,
    )
    slug = models.CharField(
        verbose_name=_("Slug"),
        max_length=120,
    )
    image = models.ImageField(
        verbose_name=_("Image"),
    )
    text = RichTextField(
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
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
