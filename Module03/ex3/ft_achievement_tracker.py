import random


ALL_ACHIEVEMENTS = [
    'World Savior', 'Master Explorer', 'Hidden Path Finder',
    'Cartographer', 'First Steps', 'Peacekeeper',
    'Boss Slayer', 'Untouchable', 'Unstoppable', 'Sharpshooter',
    'Combat Medic', 'Shadow Assassin', 'Last Man Standing',
    'Crafting Genius', 'Collector Supreme', 'Treasure Hunter',
    'Gold Digger', 'Master Alchemist',
    'Speed Runner', 'Strategist'
]


def gen_player_achievements() -> set:
    count = random.randint(8, 15)
    achievements = random.sample(ALL_ACHIEVEMENTS, count)
    return set(achievements)


def main() -> None:
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

    common = set(ALL_ACHIEVEMENTS).intersection(*players.values())
    print(f"Common achievements: {common}\n")

    for name, achs in players.items():
        others_achs = set().union(
            *(a for n, a in players.items() if n != name)
        )
        only_this_player = achs.difference(others_achs)
        print(f"Only {name} has: {only_this_player}")

    all_possible_set = set(ALL_ACHIEVEMENTS)
    for name, achs in players.items():
        missing = all_possible_set.difference(achs)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
