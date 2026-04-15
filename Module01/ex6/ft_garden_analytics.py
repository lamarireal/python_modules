#!/usr/bin/env python3

class Plant:
    class InternalSystem:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self):
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.stats = self.InternalSystem()

    @staticmethod
    def is_older_than_year(days):
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self, amount=1.0):
        self.height += amount
        self.stats._grow_calls += 1

    def age_plant(self, days=1):
        self.age += days
        self.stats._age_calls += 1

    def show(self):
        self.stats._show_calls += 1
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        status = ("blooming beautifully!" if self.is_blooming
                  else "has not bloomed yet")
        print(f"{self.name} {status}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_calls = 0

    def produce_shade(self):
        self.shade_calls += 1
        print(f"Tree {self.name} produces shade.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seeds_count = 0

    def bloom(self):
        super().bloom()
        self.seeds_count = 42

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds_count}")


def display_full_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant.stats.display()
    if isinstance(plant, Tree):
        print(f"{plant.shade_calls} shade")


def main():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_full_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_full_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_full_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_full_stats(oak)

    print("\n=== Seed")
    sun = Seed("Sunflower", 80.0, 45, "yellow")
    sun.show()
    print("[make sunflower grow, age and bloom]")
    sun.grow(30)
    sun.age_plant(20)
    sun.bloom()
    sun.show()
    display_full_stats(sun)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_full_stats(anon)


if __name__ == "__main__":
    main()
