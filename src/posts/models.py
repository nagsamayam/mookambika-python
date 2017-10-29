from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    body = models.TextField()
    draft = models.BooleanField(default=False)
    published_at = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateField(auto_now_add=False, auto_now=True)
    read_time = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title


def post_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.title = instance.title.capitalize()
    instance.body = instance.body.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(post_pre_save_receiver, Post)
