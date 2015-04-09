from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from models import Message, Msgtype

# Register your models here.


class MessageAdmin(LeafletGeoAdmin):
    list_display = ('name', 'email', 'show_location', 'created',)
    map_height = '300px'
    zoom = 13

admin.site.register(Message, MessageAdmin)
admin.site.register(Msgtype)
