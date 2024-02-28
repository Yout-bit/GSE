from django.shortcuts import render
from .models import UserProfile

# Create your views here.

def home_view(request):
    return render(request, 'home.html')
    
def coin_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'coins': user_profile.coins}
    return render(request, 'temp scan and main.html', context)