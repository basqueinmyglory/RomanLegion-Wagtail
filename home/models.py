from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel



#### Home Page ####
class HomePage(Page):
    fitness = RichTextField(blank=True)
    diet = RichTextField(blank=True)
    creed = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('fitness', classname="full"),
        FieldPanel('diet', classname="full"),
        FieldPanel('creed', classname="full"),
    ]




