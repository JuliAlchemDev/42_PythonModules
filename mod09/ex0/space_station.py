from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Validated data of a space station.

    Inheriting from BaseModel makes Pydantic check the type and the
    constraints of every field when an instance is created.
    """

    # Field() adds constraints: min_length/max_length for strings,
    # ge (>=) and le (<=) for numbers.
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)

    # Pydantic converts compatible values automatically, so a string such
    # as "2024-01-15T10:30:00" is also accepted and turned into a datetime.
    last_maintenance: datetime

    # A default value makes the field optional when creating the model.
    is_operational: bool = True

    # "str | None" allows None; default=None makes the field not required.
    notes: str | None = Field(default=None, max_length=200)


def test_valid() -> None:
    """Create a station with valid data and display it."""
    # Every field passes validation, so the instance is created.
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
    )

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print("Status: "
          f"{'Operational' if station.is_operational else 'Nonfunctional'}")

    print("")


def test_error() -> None:
    """Try to create a station with invalid data and show the error."""
    try:
        # crew_size=24 breaks the le=20 constraint, so Pydantic raises a
        # ValidationError before the instance exists.
        error_station = SpaceStation(
            station_id="ISS404",
            name="Error Space Station",
            crew_size=24,
            power_level=42.5,
            oxygen_level=90.5,
            last_maintenance=datetime.now(),
            is_operational=False
        )
        # Never reached with this data: the line above already failed.
        print("Valid station created:")
        print(f"ID: {error_station.station_id}")
        print(f"Name: {error_station.name}")
        print(f"Crew: {error_station.crew_size} people")
        print(f"Power: {error_station.power_level}%")
        print(f"Oxygen: {error_station.oxygen_level}%")
        print("Status:", end=" ")
        if error_station.is_operational:
            print("Operational")
        else:
            print("Nonfunctional")

    except ValidationError as error:
        print("Expected validation error:")
        # errors() returns one dict per failed field; "msg" holds the
        # human-readable message.
        for err in error.errors():
            print(err["msg"])


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    test_valid()
    print("========================================")
    test_error()


if __name__ == "__main__":
    main()
