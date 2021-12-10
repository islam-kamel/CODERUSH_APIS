from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import datetime
import PIL
from posts_apis.helpers.src.image_file import ImageManage


class Posts(models.Model, ImageManage):
    class PostObject(models.Manager):
        """
        This class use replace default objects().Manager() to get all data if
        published -> True
        """
        def get_queryset(self):
            return super().get_queryset().filter(published=True)

    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to=ImageManage.set_image_file,
                              blank=True, null=True)
    published = models.BooleanField(default=True)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=datetime.now)
    update_at = models.DateTimeField(auto_now_add=datetime.now)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = PostObject()

    # tags = models.ForeignKey(Tags, on_delete=models.PROTECT)

    class Meta:
        ordering = ('-create_at',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = PIL.Image.open(self.image.path)
        height, width = image.size
        image = image.resize((height, width), PIL.Image.ANTIALIAS)
        image.save(self.image.path, optimize=True, quality=90)

    def __str__(self):
        return self.title
