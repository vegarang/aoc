from year2022.day02.part1 import get_part1_points
from year2022.day02.part2 import get_part2_points


def load_file():
    with open('input.txt', 'r') as f:
        values = f.readlines()
    return values


def do_things():
    values = load_file()
    part1 = get_part1_points(values)
    part2 = get_part2_points(values)
    print(f'Part 1 total points: {part1}')
    print(f'Part 2 total points: {part2}')


if __name__ == '__main__':
    do_things()