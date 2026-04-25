import sys


def ft_score_analytics():
    print("=== Player Score Analytics ===")

    args = sys.argv[1:]
    if not args:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    valid_score = []
    for arg in args:
        try:
            score = int(arg)
            valid_score.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if not valid_score:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")
        return

    total_players = len(valid_score)
    total_score = sum(valid_score)
    average_score = total_score / total_players
    highest_score = max(valid_score)
    minimum_score = min(valid_score)
    range_score = highest_score - minimum_score

    print(f"Scores processed: {valid_score}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score:.2f}")
    print(f"High score: {highest_score}")
    print(f"Low score: {minimum_score}")
    print(f"Score range: {range_score}")


if __name__ == "__main__":
    ft_score_analytics()
