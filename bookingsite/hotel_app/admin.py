from django.contrib import admin
from .models import Hotel
from .models import Room
from .models import Booking


admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
