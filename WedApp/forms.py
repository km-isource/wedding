from django import forms
from .models import RSVP

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ["name", "email", "phone_number", "attendance", "guest_count", "message"]
