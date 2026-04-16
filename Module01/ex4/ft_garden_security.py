class Plants:
    def __init__(self, name, height, age):
        self.name = name
        self._height = 0
        self._age = 0

        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, value):
        if value < 0:
            print("Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value

    def set_age(self, value):
        if value < 0:
            print("Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value

    def show(self):
        print(f"{self.name}: {round(self._height)}cm, {self._age} days old")


def main():
    print("=== Garden Security System ===")

    rose = Plants("Rose", 15.0, 10)
    print(f"Plant created: {rose.show()}")

    rose.set_height(25.0)
    print(f"Height updated: {rose.get_height()}cm")

    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")

    print(f"{rose.name}: ", end="")
    rose.set_height(-5.0)

    print(f"{rose.name}: ", end="")
    rose.set_age(-10)

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
