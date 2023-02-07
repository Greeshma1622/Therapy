from django.contrib import admin
from .models import Plans, Counselors,Booking,Client,Contact,Room,Message

# Register your models here.
# Register your models here.
admin.site.register(Plans)
admin.site.register(Counselors)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email','counselor_name','booking_date','booked_on')

admin.site.register(Booking,BookingAdmin)
admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Room)
admin.site.register(Message)