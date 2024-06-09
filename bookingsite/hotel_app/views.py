from django.shortcuts import render, redirect


def home(request):
    return render(request, 'hotel_app/index.html',{'name':'VLad'})