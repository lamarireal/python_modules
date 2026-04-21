import sys


def ft_score_analytics():
    print("=== Player Score Analytics ===")

    if sys.argv < 2:
        print("No scores provided. Usage: python3 "
              "ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    ft_score_analytics()
