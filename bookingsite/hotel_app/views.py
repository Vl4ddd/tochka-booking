from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Hotel, Room, Booking
from .forms import BookingDate

import datetime


def home(request):
    hotels = Hotel.objects.all()
    context = {"hotels": hotels}
    return render(request, "hotel_app/index.html", context)


@login_required
def hotel(request, post_id):
    post = get_object_or_404(Hotel, pk=post_id)
    rooms = Room.objects.filter(hotel_id=post_id)
    context = {
        "rooms": rooms,
        "hotel_id": post.hotel_id,
    }

    return render(request, "hotel_app/hotel.html", context)


@login_required
def booking(request, post_id):
    try:
        booking = Booking.objects.filter(room_id=post_id)
    except:
        booking = None
    

    room = get_object_or_404(Room, pk=post_id)

    if request.method == "POST":
        form = BookingDate(request.POST)

        if form.is_valid():
            form.save(commit=False)
            Booking.user_id = request.user.id
            Booking.checkin_date = form.cleaned_data["checkin_date"]
            Booking.checkout_date = form.cleaned_data["checkout_date"]
            Booking.hotel_id = Room.objects.get(pk=post_id).hotel_id
            Booking.room_id = Room.objects.get(pk=post_id)

            form.save()
            return redirect("/")
    else:
        form = BookingDate()

    context = {
        "booking": booking,
        "room": room,
        "room_id": room.room_id,
        "data": datetime.date,
        "form": form,
    }

    return render(request, "hotel_app/booking.html", context)
