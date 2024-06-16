from django import forms
from django.core.exceptions import ValidationError

from .models import Booking

import datetime


class BookingDate(forms.ModelForm):

    checkin_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        required=True,
    )
    checkout_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        required=True,
    )

    class Meta:
        model = Booking
        fields = ["checkin_date", "checkout_date"]

    def clean(self):

        cleaned_data = super().clean()
        checkin_date = cleaned_data.get("checkin_date")
        checkout_date = cleaned_data.get("checkout_date")
        if checkin_date < datetime.date.today() or checkin_date > checkout_date:
            raise ValidationError("Выберите правильную дату")
        return cleaned_data


class Payment(forms.ModelForm):
    money = forms.IntegerField(label="Введите число", required=True)

    class Meta:
        model = Booking
        fields = ('paid',)

    
    