import math


def get_player_pos() -> tuple:
    valid_coords = []
    data = input("Enter new coordinates as floats in format 'x,y,z': ")
    coords = data.split(",")

    if len(coords) != 3:
        print("Invalid syntax")
        return get_player_pos()
    else:
        try:
            for coord in coords:
                valid_coords.append(float(coord))
        except ValueError as error:
            print(f"Error on parameter '{coord.strip()}': {error}")
            return get_player_pos()

    return tuple(valid_coords)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    first_set = get_player_pos()
    x1, y1, z1 = first_set
    print(f"Got a first tuple: {first_set}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance1 = round(math.sqrt(x1**2 + y1**2 + z1**2), 4)
    print(f"Distance to center: {distance1}")

    print("\nGet a second set of coordinates")
    second_set = get_player_pos()
    x2, y2, z2 = second_set
    distance2 = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2), 4)

    print(f"Distance between the 2 sets of coordinates: {distance2}")


if __name__ == "__main__":
    main()
