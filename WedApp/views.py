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
def messages(request):
    media = Media.objects.first()
    wedding = WeddingDetails.objects.first()
    rsvp = RSVP.objects.all()
    
    context = {
        "media": media,
        "wedding": wedding,
        "rsvp": rsvp
    }
    
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        text = request.POST.get("text", "").strip()
        
        print(f"Received data: name={name}, message={text}")
        Message.objects.create(
            name=name,
            text=text,
            
        )

    return render(request, "messages.html", context)
    
    

@csrf_exempt
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
        name = request.POST.get("field0_value", "").strip()
        email = request.POST.get("field1_value", "").strip()
        phone_number = request.POST.get("field2_value", "").strip()
        attendance = request.POST.get("field4_value", "").strip()
        guest_count = request.POST.get("field5_value", "0").strip()
        message = request.POST.get("field6_value", "").strip()
        
        print(f"Attendance: '{attendance}'")
        
        if guest_count == "":
            guest_count = 0
        
        if attendance == "":
            attendance = "yes"
        elif attendance.lower() in ["no, i will not attend", "no", "sorry, i can't come."]:
            attendance = "no"
            
        
        print(f"Processed Attendance: '{attendance}'")

        # Validate required fields
        if not name or not email or not phone_number or not attendance:
            messages.error(request, "All required fields must be filled.")
            return redirect("submit_rsvp")  # Replace with the actual RSVP page name

        # Convert guest_count safely
        try:
            guest_count = int(guest_count)
        except ValueError:
            guest_count = 0

        # Save RSVP entry
        RSVP.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            attendance=attendance,
            message=message,
            guest_count=guest_count,
        )

        messages.success(request, "Your RSVP has been submitted successfully!")
        return redirect("/")  # Redirect to the same page to show messages

    return render(request, "rsvp.html", context)