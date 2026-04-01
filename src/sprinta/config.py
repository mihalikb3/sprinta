import os
import json
from pathlib import Path
from sprinta.models import UserProfile

CONFIG_DIR = Path.home() / ".sprinta"
CONFIG_FILE = CONFIG_DIR / "profile.json"

def ensure_config_dir():
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

def save_profile(profile: UserProfile):
    ensure_config_dir()
    with open(CONFIG_FILE, "w") as f:
        f.write(profile.model_dump_json(indent=4))

def load_profile() -> UserProfile:
    if not CONFIG_FILE.exists():
        return UserProfile()
    with open(CONFIG_FILE, "r") as f:
        data = json.load(f)
        return UserProfile(**data)
