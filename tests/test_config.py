import os
import json
from pathlib import Path
import pytest
from sprinta.models import UserProfile, DayOfWeek
from sprinta.config import save_profile, load_profile, CONFIG_FILE

def test_profile_save_load(tmp_path):
    # Mock the config file path for testing
    import sprinta.config
    original_config_file = sprinta.config.CONFIG_FILE
    test_config_file = tmp_path / "profile.json"
    sprinta.config.CONFIG_FILE = test_config_file
    
    profile = UserProfile(name="Test Runner", training_days=[DayOfWeek.MONDAY])
    save_profile(profile)
    
    loaded_profile = load_profile()
    assert loaded_profile.name == "Test Runner"
    assert DayOfWeek.MONDAY in loaded_profile.training_days
    
    # Restore original path
    sprinta.config.CONFIG_FILE = original_config_file

if __name__ == "__main__":
    pytest.main([__file__])
