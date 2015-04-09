from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class PublishQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('u', 'UnPublished'),
)


class Entry(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    slug = models.CharField(max_length=200, unique=True,
                            blank=True, help_text='auto generate slug field')
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(User, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    objects = PublishQuerySet.as_manager()
    # Overide save

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()

        # self.slug = slugify(self.title)
        self.slug = "%s" % (self.title.replace(" ", "-"))
        # self.slug = "%s" % (self.title.replace(" ", "-"))

        super(Entry, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
