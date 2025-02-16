from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from .models import RSVP, WeddingDetails, Media, Message
from django.utils import timezone
from .forms import RSVPForm

def index(request):
    media = Media.objects.first()
    current_datetime = timezone.now()
    wedding = WeddingDetails.objects.first()
    context = {
        "wedding": wedding,
        "current_datetime": current_datetime,
        "media": media
    }
    return render(request, "index.html", context)

def home(request):
    media = Media.objects.first()
    current_datetime = timezone.now()
    wedding = WeddingDetails.objects.first()
    context = {
        "wedding": wedding,
        "current_datetime": current_datetime,
        "media": media
    }
    return render(request, "home.html", context)

@csrf_exempt
def add_message(request):
    media = Media.objects.first()
    wedding = WeddingDetails.objects.first()
    message = Message.objects.filter(approved=True)
    
    context = {
        "media": media,
        "wedding": wedding,
        "message": message
    }
    
    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")
        recipient = request.POST.get("recipient")
        
        Message.objects.create(
            name=name,
            text=text,
            recipient=recipient,
        )
        return redirect("messages")

    return render(request, "add_messages.html", context)

def messages(request):
    media = Media.objects.first()
    wedding = WeddingDetails.objects.first()
    message = Message.objects.filter(approved=True)
    
    context = {
        "media": media,
        "wedding": wedding,
        "message": message
    }

    return render(request, "messages.html", context)
    
    

def submit_rsvp(request):
    media = Media.objects.first()
    current_datetime = timezone.now()
    wedding = WeddingDetails.objects.first()
    context = {
        "wedding": wedding,
        "current_datetime": current_datetime,
        "media": media
    }
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        attendance = request.POST.get("attendance")
        guest_count = request.POST.get("guest_count")
        message = request.POST.get("message")
        
        
        if guest_count == "":
            guest_count = 0
        
        if attendance == "":
            attendance = "yes"
        elif attendance.lower() in ["no, i will not attend", "no", "sorry, i can't come."]:
            attendance = "no"
            
        try:
            guest_count = int(guest_count)
        except ValueError:
            guest_count = 0
            
        RSVP.objects.create(
            name=name,
            email=email,
            attendance=attendance,
            message=message,
            guest_count=guest_count,
        )
        return redirect("home")
    return render(request, "rsvp.html", context)