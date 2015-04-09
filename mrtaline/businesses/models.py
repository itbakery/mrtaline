from django.db import models
from django.contrib.gis.db import models as gismodels
from time import time
# Create your models here.


def get_upload_filename(instance, filename):
    return "upload_business/%s_%s" % (str(time()).replace('.', '_'), filename)


class PublishQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)


class Biztype(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Business(models.Model):
    biztypes = models.ManyToManyField(Biztype)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=250)
    phone = models.TextField(blank=True)
    published = models.BooleanField(default=False, blank=True)
    geom = gismodels.PointField()
    photo = models.ImageField(upload_to=get_upload_filename)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = PublishQuerySet.as_manager()

    def show_location(self):
        return "lat: %s, lng: %s" % (self.geom.y, self.geom.x)

    def save(self, *args, **kwargs):
        # Gen Slug
        self.slug = "%s" % (self.title.replace(" ", "-"))
        super(Business, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.title
