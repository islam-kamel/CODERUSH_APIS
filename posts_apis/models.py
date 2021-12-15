import PIL
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timezone import datetime
from django.conf import settings
from .helpers.src.image_file import ImageManage


class Posts(models.Model):

    class Meta:
        ordering = ('-create_at',)

    class PostObject(models.Manager):
        """
        This class use replace default objects().Manager() to get all data if
        published -> True
        """
        def get_queryset(self):
            return super().get_queryset().filter(published=True)

    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to=ImageManage.set_image_file,
                              blank=True, null=True)
    published = models.BooleanField(default=True)

    slug = models.SlugField(blank=True, max_length=120)
    create_at = models.DateTimeField(auto_now_add=datetime.now)
    update_at = models.DateTimeField(auto_now_add=datetime.now)

    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)

    objects = PostObject()

    # TODO Tags

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'pk': self.pk,
            'slug': self.slug
        }
        return reverse('post_details', kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = self.title.replace(" ", "-").lower()
        super(Posts, self).save(*args, **kwargs)
        if self.image:
            try:
                image = PIL.Image.open(self.image.path)
                height, width = image.size
                image = image.resize((height, width), PIL.Image.ANTIALIAS)
                image.save(self.image.path, optimize=True, quality=90)
            except FileNotFoundError:
                raise ValueError('can not open the image invalid path')