#!/usr/bin/env python3


from brain_games.engine import run_game
from brain_games.games.gcd import gcd_game


def main():
    run_game(gcd_game)


if __name__ == "__main__":
    main()


