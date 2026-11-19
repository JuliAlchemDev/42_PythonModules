from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Self


class ContactType(Enum):
    """
    Types of contact
    """
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = datetime.now()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_contact_rules(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if self.contact_type.value == "physical" and not self.is_verified:
            raise ValueError(
                f"{(self.contact_type.value).capitalize()} "
                "contact reports must be verified")
        if self.contact_type.value == "telepathic" and self.witness_count < 3:
            raise ValueError(
                f"{(self.contact_type.value).capitalize()} "
                "contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) "
                "should include received messages")
        return self


def test_valid() -> None:
    print("Valid contact report:")
    new_contact = AlienContact(
        contact_id="AC_2024_001",
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli"
    )

    print(f"ID: {new_contact.contact_id}")
    print(f"Type: {new_contact.contact_type.value}")
    print(f"Location: {new_contact.location}")
    print(f"Signal: {new_contact.signal_strength}/10")
    print(f"Duration: {new_contact.duration_minutes} minutes")
    print(f"Witnesses: {new_contact.witness_count}")
    print(f"Message: '{new_contact.message_received}'")
    print("")


def test_error() -> None:
    try:
        print("Expected validation error:")
        new_contact = AlienContact(
            contact_id="AC_2026_042",
            location="Carrer d'Albert Einstein, 11, Barcelona",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=9.5,
            duration_minutes=2,
            witness_count=1,
            message_received="@channel RECORDATORIO VERY MUY IMPORTANTE"
        )

        print(f"ID: {new_contact.contact_id}")
        print(f"Type: {new_contact.contact_type.value}")
        print(f"Location: {new_contact.location}")
        print(f"Signal: {new_contact.signal_strength}/10")
        print(f"Duration: {new_contact.duration_minutes} minutes")
        print(f"Witnesses: {new_contact.witness_count}")
        print(f"Message: '{new_contact.message_received}'")

    except ValidationError as error:
        for err in error.errors():
            print(err['msg'].replace("Value error, ", ""))


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    test_valid()
    print("======================================")
    test_error()


if __name__ == "__main__":
    main()
