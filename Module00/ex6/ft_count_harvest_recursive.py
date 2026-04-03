def ft_count_harvest_recursive():
    print("Days until harvest: ", end="")
    days = int(input())

    def count_up(day):
        if day <= days:
            print(f"Day {day}")
            count_up(day + 1)
        else:
            print("Harvest time!")
    count_up(1)
