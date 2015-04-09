from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gismodels
from uuidfield import UUIDField
import datetime
# Create your models here.


class Portal(models.Model):
    user = models.ForeignKey(User, related_name='portals')
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('u', 'UnPublished'),
)

REPORT_TYPES = (
    ('t', 'Traffic Jam'),
    ('c', 'Contruction'),
    ('b', 'Traffic Close'),
    ('v', 'Vibration'),
    ('w', 'Water'),
    ('n', 'Noise'),
    ('d', 'Dust'),
)


class PublishQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Place(gismodels.Model):
    # related_name must be plurals of models name
    user = models.ForeignKey(User, related_name='places')
    # portal = models.ForeignKey(Portal, related_name='portals', blank=True)
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, blank=True)
    uuid = UUIDField(auto=True)
    description = models.TextField()
    published = models.BooleanField(default=False, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default="d")
    reporttype = models.CharField(max_length=1, choices=REPORT_TYPES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    stop_date = models.DateTimeField(auto_now_add=True, blank=True)
    geom = gismodels.PointField()
    picture = models.ImageField(upload_to='places/%Y/%m/%d', blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    objects = gismodels.GeoManager()
    is_publish = PublishQuerySet.as_manager()

    def latitude(self):
        return self.location.y

    def longitude(self):
        return self.location.x

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        # Gen Slug
        self.slug = "%s" % (self.title.replace(" ", "-"))
        super(Place, self).save(*args, **kwargs)

    def image_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return '/media/images/place.png'

    @property
    def popupContent(self):
        return "<p>%s</p>" % (self.description)
        #return "<p>%s</p><img src=%s />" % (self.description,self.image_url() )
        #return self.image_url

    @property
    def marker(self):
        markerlist = {
            't' : 'car',
            'c' : 'campsite',
            'b' : 'cross',
            'v' : 'square',
            'w' : 'water',
            'n' : 'music',
            'd' : 'circle',
        }
        return markerlist[self.reporttype]

    def __unicode__(self):
        return self.title


class Area(gismodels.Model):
    user = models.ForeignKey(User, related_name='areas')
    title = models.CharField(max_length=256)
    uuid = UUIDField(auto=True)
    description = models.TextField()
    geom = gismodels.MultiPolygonField()

    objects = gismodels.GeoManager()
    is_publish = PublishQuerySet.as_manager()

    def __unicode__(self):
        return self.title
