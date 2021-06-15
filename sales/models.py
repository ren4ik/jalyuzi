from django.db import models
from django.urls import reverse
from pytils.translit import slugify
import random

from catalog.models import Product


class Order(models.Model):
    order_id = models.CharField("Order ID", default="000-000", editable=False, max_length=10)
    client_name = models.CharField("Client name", max_length=100)
    contact = models.CharField("Client contact", max_length=50)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.SET_NULL, null=True)
    pub_date = models.DateField("Publication date", auto_now_add=True)
    slug = models.SlugField("Slug url", unique=True, blank=True)
    is_delivered = models.BooleanField("Delivered", default=False)
    qty = models.PositiveSmallIntegerField("Qty", default=1)
    delivered_date = models.DateField("Delivered date", auto_now=True)

    def save(self, *args, **kwargs):
        self.order_id = f'{random.randint(100, 999)}-{random.randint(100, 999)}'
        self.slug = f'{self.order_id}-{slugify(self.client_name)}'
        super(Order, self).save(*args, **kwargs)

    def price(self):
        return self.product.price * self.qty

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.client_name
