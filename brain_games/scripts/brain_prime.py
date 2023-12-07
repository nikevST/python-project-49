#!/usr/bin/env python3


from brain_games.engine import run_game
from brain_games.games.prime import prime_game


def main():
    run_game(prime_game)


if __name__ == "__main__":
    main()
