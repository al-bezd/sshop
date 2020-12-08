from django.db import models
from django.db.models import DecimalField
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from longclaw.products.models import ProductVariantBase, ProductBase
try:
    from wagtail.wagtailcore import blocks
    from wagtail.wagtailimages.blocks import ImageChooserBlock

    wagtail_version = 1
except ImportError:
    from wagtail.core import blocks
    from wagtail.images.blocks import ImageChooserBlock
class ProductIndex(Page):
    """Index page for all products
    """
    subpage_types = ('catalog.Product', 'catalog.ProductIndex')




class Row(blocks.StructBlock):
    name  = blocks.CharBlock(
        label='name',
        max_length=64,
    )
    value = blocks.CharBlock(
        label='value',
        max_length=128,
    )
    class Meta:
        template = 'wagtail_blocks/table_row.html'
        icon = "title"

class WeLike(blocks.StructBlock):
    pass
    class Meta:
        template = 'wagtail_blocks/WeLike.html'
        icon = "title"

    @property
    def items(self):
        return Product.objects.all().by_order('?')[0:5]

class Product(ProductBase):
    parent_page_types = ['catalog.ProductIndex']
    description       = RichTextField()
    short_description = RichTextField()
    prise       = models.DecimalField(decimal_places=2, max_digits=9)
    old_price   = models.DecimalField(decimal_places=2, max_digits=9, default=0.00, blank=True)
    reviews     = models.IntegerField(default=0,blank=True)
    orders      = models.IntegerField(default=0, blank=True)
    article     = models.CharField(max_length=128)
    attr        = StreamField([('Row', Row()),], blank=True)
    we_like     = StreamField([('WeLike', WeLike())], blank=True)
    content_panels = ProductBase.content_panels + [
        FieldPanel('description'),
        FieldPanel('short_description'),
        InlinePanel('images', label='Images'),
        FieldPanel('article'),
        FieldPanel('prise'),
        FieldPanel('old_price'),
        FieldPanel('reviews'),
        FieldPanel('orders'),
        StreamFieldPanel('attr'),
        StreamFieldPanel('we_like'),
        InlinePanel('variants', label='Product variants'),

    ]

    @property
    def first_image(self):
        return self.images.first()


class ProductVariant(ProductVariantBase):
    """Represents a 'variant' of a product
    """
    # You *could* do away with the 'Product' concept entirely - e.g. if you only
    # want to support 1 'variant' per 'product'.
    product = ParentalKey(Product, related_name='variants')

    slug = AutoSlugField(
        separator='',
        populate_from=('product', 'ref'),
        )

    # Enter your custom product variant fields here
    # e.g. colour, size, stock and so on.
    # Remember, ProductVariantBase provides 'price', 'ref' and 'stock' fields
    description = RichTextField()


class ProductImage(Orderable):
    """Example of adding images related to a product model
    """
    product = ParentalKey(Product, related_name='images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, max_length=255)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption')
    ]


