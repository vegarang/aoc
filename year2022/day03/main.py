from year2022.day03.part1 import run_part_1
from year2022.day03.part2 import run_part_2


def load_file():
    with open('input.txt', 'r') as f:
        values = f.readlines()
    return values


def do_things():
    values = load_file()
    run_part_1(values)
    run_part_2(values)


if __name__ == '__main__':
    do_things()
