from garminconnect import Garmin
from sprinta.models import UserProfile

def authenticate_garmin(profile: UserProfile):
    """Authenticate with Garmin Connect."""
    client = Garmin(profile.garmin_username, profile.garmin_password)
    client.login()
    return client

def sync_workout(client: Garmin, workout_data: dict):
    """Sync a workout to Garmin Connect."""
    # This part requires mapping our workout format to Garmin's JSON format.
    # For now, it's a placeholder.
    print(f"Syncing workout: {workout_data['name']}...")
    # client.external_create_workout(workout_data)
    return True
