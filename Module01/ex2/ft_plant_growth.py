#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def age_one_day(self):
        self.age += 1

    def grow(self):
        self.height = round(self.height + self.growth_rate, 2)

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    print("=== Garden Plant Growth ===")

    start_height = 25.0
    rose = Plant("Rose", start_height, 30, 0.8)
    rose.show()

    for days in range(1, 8):
        print(f"=== Day {days} ===")
        rose.age_one_day()
        rose.grow()
        rose.show()

    print(f"Growth this week: {round(rose.height - start_height, 2)}cm")


if __name__ == "__main__":
    main()
