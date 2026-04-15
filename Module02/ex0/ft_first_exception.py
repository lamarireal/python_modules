#!/usr/bin/env python3

def input_treperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature():
    print("=== Gerden Temperature ===")
    input_cases = [25, "abc"]

    for data in input_cases:
        print(f"Input data is: '{data}'")
        try:
            temp = input_treperature(data)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
