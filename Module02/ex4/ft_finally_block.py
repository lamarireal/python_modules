class PlantError(Exception):
    def __init__(self, message="Invalid plant name"):
        super().__init__(message)


def water_plant(plant_name: str):
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants_list):
    print("Opening watering system")
    try:
        for plant in plants_list:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main():
    print("=== Garden Watering System ===")
    
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    
    print("\nTesting invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
