from django.db import models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailsearch import index
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey



class AuthorsIndexPage(Page):
    intro = RichTextField(blank=True)



    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(AuthorsIndexPage, self).get_context(request)
        authorpage = self.get_children().live().order_by('title')
        context['authorpage'] = authorpage
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class AuthorPage(Page):
    height = models.CharField(max_length=25)
    age = models.CharField(max_length=2)
    location = models.CharField(max_length=250)
    routine = models.CharField(max_length=50)
    diet = models.CharField(max_length=50)
    myfitnesspal = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(AuthorPage, self).get_context(request)

        blogpage = BlogIndexPage.get_children(self).live()
        context['blogpage'] = blogpage
        return context

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('height'),
        FieldPanel('age'),
        FieldPanel('location'),
        FieldPanel('routine'),
        FieldPanel('diet'),
        FieldPanel('myfitnesspal'),
        FieldPanel('instagram'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class AuthorPageGalleryImage(Orderable):
    page = ParentalKey(AuthorPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]




class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndexPage, self).get_context(request)
        blogpage = self.get_children().live().order_by('title')
        context['blogpage'] = blogpage
        return context

    

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class BlogPage(Page):
    date = models.DateField("Post date")
    author = models.CharField(max_length=50)
    body = RichTextField(blank=True)


    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('body', classname="full"),
    ]