from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from models import Place, Area, Portal
# Register your models here.
class ReportAdmin(LeafletGeoAdmin):
    list_display = ('title',)
    #map_width = '90%'
    map_height = '500px'

admin.site.register(Place, ReportAdmin)
admin.site.register(Area, ReportAdmin)
admin.site.register(Portal)
