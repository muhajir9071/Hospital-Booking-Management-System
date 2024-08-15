from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['field4']  # Specify the fields you want to exclude
