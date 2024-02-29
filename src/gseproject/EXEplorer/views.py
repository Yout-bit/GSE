from django.shortcuts import render
from .models import UserProfile
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return render(request, 'home.html')
    

def scanner_view(request):
    return render(request, 'game/qr_scanner.html')

def game_view(request):
    try:
        # Attempt to get the UserProfile associated with the request.user
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # If the UserProfile does not exist, create a new one
        user_profile = UserProfile.objects.create(user=request.user)
    context = {'coins': user_profile.coins}
    return render(request, 'temp scan and main.html', context)
