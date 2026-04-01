import sys
from pathlib import Path

# Add the parent directory of sprinta/ to sys.path to allow direct execution
src_path = str(Path(__file__).parent.parent)
if src_path not in sys.path:
    sys.path.insert(0, src_path)

import typer
from sprinta.ui import run_dashboard
from sprinta.config import load_profile, save_profile
from sprinta.models import DayOfWeek

app = typer.Typer(help="Sprinta: AI Running Coach CLI")

@app.command()
def setup():
    """Set up your user profile and Garmin credentials."""
    profile = load_profile()
    typer.echo(f"Hello, {profile.name}! Setting up your profile.")
    
    name = typer.prompt("What's your name?", default=profile.name)
    profile.name = name
    
    race_goal = typer.prompt("Which race are you training for? (e.g. 5k, 10k, Marathon)", default=profile.race_goal or "5k")
    profile.race_goal = race_goal
    
    weekly_mileage = typer.prompt("What's your current weekly mileage target? (km)", default=profile.weekly_mileage_target or 20.0, type=float)
    profile.weekly_mileage_target = weekly_mileage
    
    weights = typer.confirm("Do you want to include strength training?", default=profile.weights_included)
    profile.weights_included = weights
    
    garmin_user = typer.prompt("Garmin Connect Username", default=profile.garmin_username or "")
    profile.garmin_username = garmin_user
    
    garmin_pass = typer.prompt("Garmin Connect Password", hide_input=True)
    profile.garmin_password = garmin_pass
    
    save_profile(profile)
    typer.echo("Profile saved successfully!")

@app.command()
def plan():
    """Generate or view your training plan."""
    profile = load_profile()
    if not profile.garmin_username:
        typer.echo("Please run 'setup' first to configure your profile.")
        raise typer.Exit()
    
    typer.echo("Opening training plan dashboard...")
    run_dashboard()

from sprinta.ai import generate_workout

@app.command()
def recommend():
    """Get an AI-recommended workout based on scientific papers."""
    profile = load_profile()
    typer.echo("Analyzing scientific papers and your profile...")
    workout = generate_workout(profile)
    typer.echo("\n--- Recommended Workout ---")
    typer.echo(workout)

from sprinta.garmin import authenticate_garmin

@app.command()
def sync():
    """Sync your training plan to Garmin Connect."""
    profile = load_profile()
    if not (profile.garmin_username and profile.garmin_password):
        typer.echo("Please run 'setup' first to configure your Garmin credentials.")
        raise typer.Exit()
    
    typer.echo("Syncing to Garmin Connect...")
    try:
        client = authenticate_garmin(profile)
        typer.echo("Successfully authenticated with Garmin!")
        # TODO: Implement full sync logic
    except Exception as e:
        typer.error(f"Failed to authenticate with Garmin: {str(e)}")

if __name__ == "__main__":
    app()
