from django.shortcuts import render
from .models import UserProfile, ScannedNumber
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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

    carbon_footprint = user_profile.carbonFootprint

    context = {'cherries': user_profile.cherries,'CarbonFootprint':carbon_footprint}
    
    return render(request, 'game/temp scan and main.html', context)

def scanner_view(request):
    return render(request, 'game/QR code.html')

@login_required
def handle_scanned_number(request):
    if request.method == 'POST':
        scanned_number = request.POST.get('scanned_number')
        if scanned_number:
            try:
                # Retrieve the user profile associated with the current user
                user_profile = request.user.userprofile
                
                # Update the carbonFootprint field with the scanned number

                user_profile.carbonFootprint += int(scanned_number)
                user_profile.cherries += 10
                user_profile.save()
                
                # Create a new instance of ScannedNumber model and save it to the database
                ScannedNumber.objects.create(number=scanned_number)
                
                return JsonResponse({'success': True})
            except UserProfile.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'User profile does not exist'})
        else:
            return JsonResponse({'success': False, 'error': 'Scanned number not provided'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

@login_required
def reset_user_profile(request):
    if request.method == 'POST':
        # Retrieve the user profile associated with the current user
        user_profile = request.user.userprofile
        
        # Set all the fields of the user profile to their initial values
        user_profile.carbonFootprint = 5
        user_profile.cherries = 20  # Assuming you've added the cherries field
        
        # Save the updated user profile
        user_profile.save()
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
def get_carbon_footprint_value(request):
    # Fetch the current user's carbon footprint value

    carbon_footprint_value = request.user.userprofile.carbonFootprint

    # Return the value as a JSON response
    return JsonResponse({'carbon_footprint_value': carbon_footprint_value})

def get_cherries_value(request):
    # Fetch the current user's cherries value
    cherries_value = request.user.userprofile.cherries
    # Return the value as a JSON response
    return JsonResponse({'cherries_value': cherries_value})
    
def shop_view(request):
    return render(request, 'game/shop.html')

def tree_view(request):
    return render(request, 'game/tree.html')
