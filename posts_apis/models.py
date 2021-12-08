from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import datetime

from .helpers.image_file import ImageManage

image_manage = ImageManage()


class Posts(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to=image_manage.set_image_file, blank=True)
    published = models.BooleanField(default=True)
    slug = models.SlugField()
    create_at = models.DateTimeField(auto_now_add=datetime.now)
    update_at = models.DateTimeField(auto_now_add=datetime.now)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # tags = models.ForeignKey(Tags, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
