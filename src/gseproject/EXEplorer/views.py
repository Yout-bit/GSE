from django.shortcuts import render
from .models import UserProfile
from django.http import JsonResponse

def home_view(request):
    return render(request, 'home.html')


def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)

def game_view(request):
    try:
        # Attempt to get the UserProfile associated with the request.user
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # If the UserProfile does not exist, create a new one
        user_profile = UserProfile.objects.create(user=request.user)
    context = {'coins': user_profile.coins}
    return render(request, 'game/temp scan and main.html', context)

def scanner_view(request):
    return render(request, 'game/QR code.html')
