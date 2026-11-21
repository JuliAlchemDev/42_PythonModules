from enum import Enum
from datetime import datetime
from typing import Union, Any, Self
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(Enum):
    """Crew ranks; the Enum restricts the field to these values."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Validated data of a single crew member."""

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """Validated mission that contains a list of crew members."""

    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)

    # Nested model: every item of the list is validated as a CrewMember.
    # Pydantic also converts plain dicts into CrewMember instances, and
    # min_length/max_length limit the size of the list (1-12 members).
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    # Runs after all fields (and every nested CrewMember) are valid, so
    # here the whole crew can be checked safely.
    @model_validator(mode='after')
    def validate_mission(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        # any() is True as soon as one member is Commander or Captain.
        if not any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        ):
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        # Long missions need at least half of the crew with 5+ years.
        if self.duration_days > 365:
            experienced_crew = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_crew += 1

            total_crew = len(self.crew)
            if experienced_crew < total_crew / 2:
                raise ValueError(
                    "Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)")

        # all() is True only if every member is active.
        if not all(
            member.is_active for member in self.crew
        ):
            raise ValueError("All crew members must be active")
        return self


def create_mission(data: dict[str, Any]) -> Union[SpaceMission, None]:
    """Build a mission from a dict; print the errors and return None
    if the data does not pass validation."""
    try:
        # **data unpacks the dict into keyword arguments of the model.
        return SpaceMission(**data)
    except ValidationError as error:
        print("Expected validation error:")
        # Pydantic adds the "Value error, " prefix to messages coming from
        # a ValueError, so it is removed to show only our own text.
        for err in error.errors():
            print(err['msg'].replace("Value error, ", ""))
        return None


def show_mission(mission: SpaceMission) -> None:
    """Display the mission details and its crew."""
    try:
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")

        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        # Each item of mission.crew is a CrewMember, not a dict.
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"- {member.specialization}"
            )
        print("")
    except Exception as error:
        print(f"{error}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    # Valid mission: it has a Commander, all crew members are active and
    # all of them have 5+ years of experience.
    valid_data = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": datetime(2020, 5, 17, 17, 42),
        "duration_days": 900,
        "crew": [
            {
                "member_id": "C001",
                "name": "Sarah Connor",
                "rank": Rank.COMMANDER,
                "age": 45,
                "specialization": "Mission Command",
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
        print("Valid mission created:")
        show_mission(new_mission)

    print("=========================================")

    # Invalid mission: no crew member is Commander or Captain, so the
    # custom validator rejects it.
    invalid_data = {
        "mission_id": "M2024_ALPHA",
        "mission_name": "Alpha Centauri Expedition",
        "destination": "Alpha Centauri",
        "launch_date": datetime(2020, 5, 17, 17, 42),
        "duration_days": 900,
        "crew": [
            {
                "member_id": "C001",
                "name": "Ye Wenjie",
                "rank": Rank.OFFICER,
                "age": 45,
                "specialization": "Mission Command",
                "years_experience": 20,
                "is_active": True
            },
            {
                "member_id": "C002",
                "name": "Wang Miao",
                "rank": Rank.LIEUTENANT,
                "age": 35,
                "specialization": "Navigation",
                "years_experience": 10,
                "is_active": True
            },
            {
                "member_id": "C003",
                "name": "Shi Qiang",
                "rank": Rank.CADET,
                "age": 30,
                "specialization": "Engineering",
                "years_experience": 8,
                "is_active": True
            }
        ],
        "budget_millions": 2500.0
    }

    failed_mission = create_mission(invalid_data)
    if failed_mission:
        show_mission(failed_mission)


if __name__ == "__main__":
    main()
