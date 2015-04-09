from django.db import models
from time import time
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
# Create your models here.


class PublishQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)


def get_upload_filename(instance, filename):
    return "upload_message/%s_%s" % (str(time()).replace('.', '_'), filename)


class Msgtype(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Message(models.Model):
    msgtypes = models.ManyToManyField(Msgtype)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=75)
    message = models.TextField()
    published = models.BooleanField(default=False, blank=True)
    latlng = models.CharField(max_length=250, blank=True)
    geom = gismodels.PointField()
    photo = models.ImageField(upload_to=get_upload_filename)
    created = models.DateTimeField(auto_now_add=True)

    objects = PublishQuerySet.as_manager()

    def latitude(self):
        return self.geom.y

    def longitude(self):
        return self.geom.x

    def show_location(self):
        return "latitude: %s, longitude: %s" % (self.geom.y, self.geom.x)

    def save(self, *args, **kwargs):
        print self.latlng
        latlng = self.latlng.split(',')
        print float(latlng[0])
        print float(latlng[1])
        if not self.geom:
            self.geom = Point(float(latlng[1]), float(latlng[0]))

        super(Message, self).save()

    def __unicode__(self):
        return self.name
