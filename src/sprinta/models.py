from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class DayOfWeek(str, Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"

class UserProfile(BaseModel):
    name: str = "Runner"
    training_days: List[DayOfWeek] = Field(default_factory=lambda: [DayOfWeek.TUESDAY, DayOfWeek.THURSDAY, DayOfWeek.SATURDAY])
    weights_included: bool = False
    race_goal: Optional[str] = None
    target_date: Optional[str] = None
    weekly_mileage_target: Optional[float] = None
    garmin_username: Optional[str] = None
    garmin_password: Optional[str] = None
