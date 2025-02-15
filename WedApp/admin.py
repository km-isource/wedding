from django.contrib import admin
from .models import WeddingDetails, Media, RSVP, Message

# Register your models here.
class WeddingDetailsAdmin(admin.ModelAdmin):
    list_display = ('bride', 'groom', 'date', 'ceremony_time')
    
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'attendance', 'message', 'guest_count')

admin.site.register(WeddingDetails, WeddingDetailsAdmin)
admin.site.register(Media)
admin.site.register(RSVP, RSVPAdmin)
admin.site.register(Message)