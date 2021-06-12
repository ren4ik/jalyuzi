from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from pytils.translit import slugify


class ProductCategory(models.Model):
    name = models.CharField("Category name", max_length=100)
    is_active = models.BooleanField("Active?", default=False)
    slug = models.SlugField("Slug url", unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Products Category'

    def get_absolute_url(self):
        return reverse('category-product-detail', kwargs={'slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        verbose_name="Category",
        related_name="cat_name",
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField("Title SEO", max_length=100)
    description = models.CharField("Description", max_length=200)
    h1 = models.CharField("Title in text (h1)", max_length=100)
    img = models.ImageField("Photo", upload_to="news", default="Not image")
    text = RichTextField("Content")
    price = models.PositiveIntegerField("Price", default=0)
    pub_date = models.DateField("Publication Date", auto_now_add=True)
    is_active = models.BooleanField("Active?", default=False)
    is_new = models.BooleanField("New?", default=False)
    is_popular = models.BooleanField("Popular?", default=False)
    slug = models.SlugField("Slug url", unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def admin_image(self):

        if self.img:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.img.url}" target="_blank"><img src="{self.img.url}" width="100" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})
