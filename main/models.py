from django.db import models
from pytils.translit import slugify
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField("Name", max_length=100, default="Client", blank=True)
    phone = models.CharField("Phone", max_length=20, default="+998 99 999 99 99")
    text = models.TextField("Text", blank=True, default="From main page")
    pub_date = models.DateField("Publication date", auto_now_add=True)
    slug = models.SlugField("Slug url", unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Contact, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
