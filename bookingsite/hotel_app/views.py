from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Hotel, Room


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

    return render(request, "hotel_app/post.html", context)
