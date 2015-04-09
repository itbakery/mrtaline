from django.db import models

# Create your models here.


class PublishQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)


class Announce(models.Model):
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, blank=True)
    description = models.TextField()
    published = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = PublishQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.slug = "%s" % (self.title.replace(" ", "-"))
        super(Announce, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
