from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Bares(models.Model):
    name = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Bares, self).save(*args, **kwargs)

    def __unicode__(self):  
        return self.name

    class Meta:
        verbose_name_plural = "Bares"


class Tapas(models.Model):
    bares = models.ForeignKey(Bares)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):  
        return self.title

    class Meta:
        verbose_name_plural = "Tapas"


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
