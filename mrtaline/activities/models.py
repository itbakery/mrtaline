from django.db import models

# Create your models here.


def get_upload_filename(instance, filename):
    return "upload_activity/%s_%s" % (str(time()).replace('.', '_'), filename)

class PublishQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)


class Activity(models.Model):
    title = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, blank=True)
    description = models.TextField()
    published = models.BooleanField(default=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to=get_upload_filename, blank=True)

    objects = PublishQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.slug = "%s" % (self.title.replace(" ", "-"))
        super(Activity, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Activity Entry"
        verbose_name_plural = "Activities"
        ordering = ["-created"]
