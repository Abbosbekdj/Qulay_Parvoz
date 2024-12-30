from django.contrib import admin

from .models import *

# Django admin panelida biz yaratgan modellar ko'rinishi uchun yozilgan buyruqlar
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['city', 'airport', 'code', 'country']

class WeekAdmin(admin.ModelAdmin):
    list_display = ['number', 'name']

class FlightAdmin(admin.ModelAdmin):
    list_display = ['origin', 'destination', 'depart_time', 'duration', 'arrival_time', 'plane', 'airline', 'economy_fare', 'business_fare', 'first_fare']

class PessengerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender']

class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'ref_no', 'booking_date']
    
admin.site.register(Place, PlaceAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PessengerAdmin)
admin.site.register(User)
admin.site.register(Ticket, TicketAdmin)