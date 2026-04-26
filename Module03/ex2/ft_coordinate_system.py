import math


def get_player_pos():
    while True:
        try:
            line = input("Enter new coordinates as floats in format 'x,y,z': ")
            parts = line.split(",")

            if len(parts) != 3:
                print("Invalid syntax")
                continue

            coords = [float(p.strip()) for p in parts]

            return tuple(coords)

        except ValueError as e:
            err_val = str(e).split(':')[-1].strip()
            print(f"Error on parameter {err_val}: {e}")
        except Exception as e:
            print(f"Invalid syntax: {e}")


def calculate_distance(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dz = p2[2] - p1[2]
    return math.sqrt(dx**2 + dy**2 + dz**2)


def main():
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center = calculate_distance((0.0, 0.0, 0.0), pos1)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()

    dist_between = calculate_distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_between, 4)}")


if __name__ == "__main__":
    main()
