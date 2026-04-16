def input_treperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(
            f"Caught input_temperature error: {temp}°C is too hot"
            f" for plants (max 40°C)"
        )
    return temp


def test_temperature():
    print("=== Gerden Temperature ===")
    input_cases = [25, "abc", 100, -50]

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
