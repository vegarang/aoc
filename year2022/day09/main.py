from year2022.day09.Rope import Rope


def load_file():
    with open('input.txt', 'r') as f:
        values = f.readlines()
    return values


def run_part_1(values):
    rope = Rope(number_of_knots=2)
    rope.handle_moves(moves=values)
    result = rope.get_unique_tail_positions()

    print(f'part1: {result}')


def run_part_2(values):
    rope = Rope(number_of_knots=10)
    rope.handle_moves(moves=values)
    result = rope.get_unique_tail_positions()

    print(f'part2: {result}')


def do_things():
    values = load_file()
    run_part_1(values=values)
    run_part_2(values=values)


if __name__ == '__main__':
    do_things()
