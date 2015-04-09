from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from models import Business, Biztype
# Register your models here.


class BusinessAdmin(LeafletGeoAdmin):
    list_display = ('title','show_location','created','modified',)
    map_height = '400px'


admin.site.register(Business,BusinessAdmin)
admin.site.register(Biztype)
