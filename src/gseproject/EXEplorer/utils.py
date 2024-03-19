from django.contrib.auth.models import User
from .models import UserProfile

# Assuming you have the user instance available (e.g., logged-in user)
def check_carbon_footprint(user):
    try:
        # Retrieve the user's profile
        user_profile = UserProfile.objects.get(user=user)
        
        # Check if the user has a value for the carbonFootprint attribute
        if user_profile.carbonFootfrint is not None:
            # User has a value for carbonFootprint
            return True
        else:
            # User does not have a value for carbonFootprint
            return False
    except UserProfile.DoesNotExist:
        # UserProfile does not exist for this user
        return False

# Example usage:
# user = User.objects.get(username='example_username')
# has_carbon_footprint = check_carbon_footprint(user)
# print(has_carbon_footprint)