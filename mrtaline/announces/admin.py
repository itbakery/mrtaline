from django.contrib import admin
from models import Announce
# Register your models here.


class AnnounceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified',)

admin.site.register(Announce, AnnounceAdmin)
