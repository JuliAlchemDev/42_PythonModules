import random
import typing


PLAYERS = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan",
    "Fiona", "George", "Hannah", "Ivan", "Julia",
    "Kevin", "Laura", "Mike", "Nora", "Oscar",
    "Paula", "Quentin", "Rachel", "Sam", "Tina"
]

ACTIONS = [
    "attack", "defend", "heal", "run", "jump",
    "dodge", "block", "cast", "shoot", "charge",
    "steal", "hide", "search", "trade", "build",
    "repair", "explore", "wait", "follow", "retreat"
]


def gen_event() -> typing.Generator[tuple[str, str]]:
    while True:
        name, action = (random.choice(PLAYERS), random.choice(ACTIONS))
        yield (name, action)


def consume_event(events_list:
                  list[tuple[str, str]]) -> typing.Generator[tuple[str, str]]:
    while len(events_list):
        get_event = events_list.pop(random.randint(0, len(events_list) - 1))
        yield get_event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    event = gen_event()

    for i in range(1000):
        name, action = next(event)
        print(f"Event {i}: Player {name} did action {action}")

    events: list[tuple[str, str]] = []
    for _ in range(10):
        name, action = next(event)
        events.append((name, action))
    print(f"Built list of 10 events: {events}")

    for get_event in consume_event(events):
        print(f"Got event from list: {get_event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
