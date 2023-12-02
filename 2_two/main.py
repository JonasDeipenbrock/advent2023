import os
import re


def get_input() -> list[str]:
    with open(__file__.rstrip("main.py") + "input.txt", "r") as f:
        return f.readlines()


def solve_a(input: list[str]):
    RED_MAX = 12
    GREEN_MAX = 13
    BLUE_MAX = 14

    sum = 0
    power = 0
    for line in input:
        raw_game, raw_sets = line.split(":")
        match = re.search("^Game (\d+)", raw_game)
        game = int(match.group(1))
        sets = raw_sets.split(";")
        possible = True
        red_min = 0
        blue_min = 0
        green_min = 0
        for set in sets:
            red_cubes = 0
            blue_cubes = 0
            green_cubes = 0
            red_cubes_match = re.search("(\d+) red", set)
            if red_cubes_match:
                red_cubes = int(red_cubes_match.group(1))
                red_min = max(red_min, red_cubes)
            blue_cubes_match = re.search("(\d+) blue", set)
            if blue_cubes_match:
                blue_cubes = int(blue_cubes_match.group(1))
                blue_min = max(blue_min, blue_cubes)
            green_cubes_match = re.search("(\d+) green", set)
            if green_cubes_match:
                green_cubes = int(green_cubes_match.group(1))
                green_min = max(green_min, green_cubes)
            if red_cubes > RED_MAX or blue_cubes > BLUE_MAX or green_cubes > GREEN_MAX:
                possible = False
        if possible:
            sum += game
        print(red_min, green_min, blue_min)
        power += red_min * green_min * blue_min
    print("Sum")
    print(sum)
    print(power)


def solve_b(input: list[str]):
    pass


if __name__ == "__main__":
    input = get_input()
    solve_a(input)
    solve_b(input)
