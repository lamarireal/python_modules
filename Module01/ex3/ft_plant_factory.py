class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {round(self.height)}cm, {self.age} days old")


def main():
    print("=== Plant Factory Output ===")

    garden = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]

    for plant in garden:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
