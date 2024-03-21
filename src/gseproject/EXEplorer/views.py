from django.shortcuts import render
from .models import UserProfile, ScannedNumber 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import timedelta
from django.db import models

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
    
    return render(request, 'game/game_home.html', context)

def scanner_view(request):
    return render(request, 'game/QR code.html')

@login_required
def handle_scanned_number(request):
    if request.method == 'POST':
        scanned_number = request.POST.get('scanned_number')
        if scanned_number:
            try:
                
                user_profile = request.user.userprofile
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



def increment_carbon_footprint(request):
    if request.method == 'POST':
        
        user_profile = request.user.userprofile
        
        # Increment the carbon footprint value by 1
        user_profile.carbonFootprint += 1

        # Check if the carbon footprint exceeds 10
        if user_profile.carbonFootprint > 10:
            user_profile.carbonFootprint = 10
        user_profile.save()
        
        # Return a JSON response indicating success and the new carbon footprint value
        return JsonResponse({'success': True, 'new_carbon_footprint_value': user_profile.carbonFootprint})
    else:
        # Return a JSON response with an error message if the request method is not POST
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)

def decrement_carbon_footprint(request):
    if request.method == 'POST':
        user_profile = request.user.userprofile
        
        # Decrement the carbon footprint value by 2
        user_profile.carbonFootprint -= 2

        # Check if the carbon footprint goes below 0
        if user_profile.carbonFootprint < 0:
            user_profile.carbonFootprint = 0

        # Save the updated profile
        user_profile.save()
        
        # Return a JSON response indicating success and the new carbon footprint value
        return JsonResponse({'success': True, 'new_carbon_footprint_value': user_profile.carbonFootprint})
    else:
        # Return a JSON response with an error message if the request method is not POST
        return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)
    
def get_cherries_value(request):
    cherries_value = request.user.userprofile.cherries
    # Return the value as a JSON response
    return JsonResponse({'cherries_value': cherries_value})

@login_required
def update_cherries_value(request):
    if request.method == 'POST':
        try:
            cherries_value = int(request.POST.get('cherries_value', ''))
            user_profile = request.user.userprofile
            user_profile.cherries = cherries_value
            user_profile.save()
            return JsonResponse({'success': True, 'message': 'Cherries value updated successfully.'})
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Invalid cherries value.'}, status=400)
        except UserProfile.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'User profile not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'An error occurred.'}, status=500)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=405)
    
def shop_view(request):
    return render(request, 'game/shop.html')

def tree_view(request):
    return render(request, 'game/tree.html')

def scan_view(request):
    return render(request, 'game/scan.html')

@require_POST
@login_required
def petDisappear(request):
    player, _ = UserProfile.objects.get_or_create(user=request.user)
    player.pet_visible = False
    player.next_pet_appearance = timezone.now() + timedelta(minutes=60)
    player.save()
    
    return JsonResponse({"visible":player.pet_visible, "nextshow":player.next_pet_appearance})

@require_POST
@login_required
def petCheck(request):
    player, _ = UserProfile.objects.get_or_create(user=request.user)
    
    if player.pet_visible == False and player.next_pet_appearance <= timezone.now():
        player.pet_visible = True
        player.next_pet_appearance = models.DateTimeField(null=True, blank=True)
        player.save()
    
        return JsonResponse({"visible":player.pet_visible, "nextshow":player.next_pet_appearance})
    
    else:
        return JsonResponse({})