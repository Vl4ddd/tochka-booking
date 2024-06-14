from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.urls import reverse

from .models import Hotel, Room, Booking
from .forms import BookingDate, Payment

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
        booking = Booking.objects.filter(room_id=post_id, paid = True)
    except:
        booking = None
    

    room = get_object_or_404(Room, pk=post_id)

    if request.method == "POST":
        form = BookingDate(request.POST)

        if form.is_valid():
                
                form.save(commit=False)
                form.instance.user = request.user
                Booking.checkin_date = form.cleaned_data["checkin_date"]
                Booking.checkout_date = form.cleaned_data["checkout_date"]
                form.instance.hotel_id = Room.objects.get(pk=post_id).hotel_id
                form.instance.room_id = Room.objects.get(pk=post_id)

                model = form.save()
                form.save()
                request.session['booking_id'] = model.booking_id
                
            
                return redirect(f'payment/', post_id=post_id)
            
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


def payment(request, post_id):

    room = get_object_or_404(Room, pk=post_id)

    book_paid = Booking.objects.get(pk = request.session['booking_id'])

    if request.method == "POST":
        form = Payment(request.POST, instance=book_paid)
            
        if form.is_valid():  
            money = form.cleaned_data['money']
            if int(money) == int(Room.objects.get(pk=post_id).price):
                form.instance.paid = True
                form.save()


                return redirect(reverse('users/profile'))
            else:
                form.add_error('money', 'Money-')

                            
    else:
        form = Payment(instance=book_paid)

    context = {
    "room": room,
    "room_id": room.room_id,
    'form': form,
    }

    
    return render(request, "hotel_app/payment.html", context)

   
   

   
