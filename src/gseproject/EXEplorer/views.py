from django.shortcuts import render
from .models import UserProfile
from django.http import JsonResponse
from .models import ScannedNumber

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
    carbon_footprint = user_profile.carbonFootfrint
    context = {'coins': user_profile.coins,'CarbonFootprint':carbon_footprint}
    
    return render(request, 'game/temp scan and main.html', context)

def scanner_view(request):
    return render(request, 'game/QR code.html')

def handle_scanned_number(request):
    if request.method == 'POST':
        scanned_number = request.POST.get('scanned_number')
        print(scanned_number)
        if scanned_number:
            #  Create a new instance of ScannedNumber model and save it to the database
            new_scanned_number=ScannedNumber.objects.create(number=scanned_number)
            # Retrieve the number you just created
            created_number = new_scanned_number.number
            # Print the created number on the console
            print("Created number:", created_number)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Scanned number not provided'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def shop_view(request):
    return render(request, 'game/shop.html')

def tree_view(request):
    return render(request, 'game/tree.html')