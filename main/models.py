from django.db import models
from pytils.translit import slugify
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField("Name", max_length=100, default="Client", blank=True)
    phone = models.CharField("Phone", max_length=20, default="+998 99 999 99 99")
    text = models.TextField("Text", blank=True, default="From main page")
    pub_date = models.DateField("Publication date", auto_now_add=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name


class Slider(models.Model):
    img = models.ImageField("Photo", upload_to="slider")
    title = models.CharField("Title slide", max_length=100)
    is_active = models.BooleanField("Active?", default=False)

    def admin_image(self):

        if self.img == 'Not image':
            return 'Not Image Found'
        elif self.img:
            from django.utils.safestring import mark_safe
            return mark_safe(
                f'<a href="{self.img.url}" target="_blank"><img src="{self.img.url}" width="100" /></a>'
            )
        else:
            return 'Not Image Found'

    admin_image.short_description = 'Photo'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'

    def __str__(self):
        return self.title
