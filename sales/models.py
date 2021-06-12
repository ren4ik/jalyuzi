from django.db import models
from django.urls import reverse
from pytils.translit import slugify

from catalog.models import Product


class Order(models.Model):
    client_name = models.CharField("Client name", max_length=100)
    contact = models.CharField("Client contact", max_length=50)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.SET_NULL, null=True)
    pub_date = models.DateField("Publication date", auto_now_add=True)
    slug = models.SlugField("Slug url", unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.client_name)
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'slug': self.slug})
