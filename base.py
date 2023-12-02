import os


def get_input() -> list[str]:
    with open(__file__.rstrip("main.py") + "input.txt", "r") as f:
        return f.readlines()


def solve_a(input: list[str]):
    pass


def solve_b(input: list[str]):
    pass


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
