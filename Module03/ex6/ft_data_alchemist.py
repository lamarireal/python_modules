import random


def main():
    print("=== Game Data Alchemist ===")

    players = ['Alice', 'bob', 'Charlie', 'dylan',
               'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    all_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")

    original_caps = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {original_caps}")

    scores = {name: random.randint(0, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")

    avg_score = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg_score, 2)}")

    high_scores = {
        name: score for name, score in scores.items()
        if score > avg_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
