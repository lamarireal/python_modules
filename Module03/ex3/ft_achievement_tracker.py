import random


ALL_POSSIBLE_ACHIEVEMENTS = [
    'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme',
    'Untouchable', 'Boss Slayer', 'Strategist', 'Unstoppable', 'Speed Runner',
    'Survivor', 'Treasure Hunter', 'First Steps', 'Sharp Mind',
    'Hidden Path Finder'
]


def gen_player_achievements():
    count = random.randint(3, 9)
    achievements = random.sample(ALL_POSSIBLE_ACHIEVEMENTS, count)
    return set(achievements)


def main():
    print("=== Achievement Tracker System ===\n")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    for name, achs in players.items():
        print(f"Player {name}: {achs}")

    all_unlocked = set().union(*players.values())
    print(f"\nAll distinct achievements: {all_unlocked}\n")

    common = set(ALL_POSSIBLE_ACHIEVEMENTS).intersection(*players.values())
    print(f"Common achievements: {common}\n")

    for name, achs in players.items():
        others_achs = set().union(
            *(a for n, a in players.items() if n != name)
        )
        only_this_player = achs.difference(others_achs)
        print(f"Only {name} has: {only_this_player}")

    all_possible_set = set(ALL_POSSIBLE_ACHIEVEMENTS)
    for name, achs in players.items():
        missing = all_possible_set.difference(achs)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
