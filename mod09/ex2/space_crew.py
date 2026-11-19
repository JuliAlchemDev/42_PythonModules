from enum import Enum
from datetime import datetime
from typing import Union, Any
from pydantic import BaseModel, Field, ValidationError


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)


def create_mission(data: dict[str, Any]) -> Union[SpaceMission, None]:
    try:
        print("Valid mission created:")
        return SpaceMission(**data)
    except ValidationError as error:
        print("Expected validation error:")
        for err in error.errors():
            print(err["msg"])


def show_mission(mission: SpaceMission) -> None:
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    valid_data = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date":  datetime(2020, 5, 17, 17, 42),
        "duration_days": 900,
        "crew": [
            {
                "member_id": "C001",
                "name": "Sarah Connor",
                "rank": Rank.COMMANDER,
                "age": 45,
                "specialization": "Leadership",
                "years_experience": 20,
                "is_active": True
            },
            {
                "member_id": "C002",
                "name": "John Smith",
                "rank": Rank.LIEUTENANT,
                "age": 35,
                "specialization": "Navigation",
                "years_experience": 10,
                "is_active": True
            },
            {
                "member_id": "C003",
                "name": "Alice Johnson",
                "rank": Rank.OFFICER,
                "age": 30,
                "specialization": "Engineering",
                "years_experience": 8,
                "is_active": True
            }
        ],
        "budget_millions": 2500.0
    }
    new_mission = create_mission(valid_data)
    if new_mission:
        show_mission(new_mission)


if __name__ == "__main__":
    main()
