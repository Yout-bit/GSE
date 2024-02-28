from django.shortcuts import render
from .models import UserProfile

def game_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    context = {'coins': user_profile.coins}
    return render(request, 'your_template.html', context)
