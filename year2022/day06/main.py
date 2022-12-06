from year2022.day06.marker import get_next_marker


def load_file():
    with open('input.txt', 'r') as f:
        values = f.readlines()
    return values


def run_part_1(values):
    marker = get_next_marker(values=values, marker_length=4)
    print(f'part1, marker: {marker}')


def run_part_2(values):
    marker = get_next_marker(values=values, marker_length=14)
    print(f'part2, marker: {marker}')


def do_things():
    values = load_file()[0]
    run_part_1(values)
    run_part_2(values)


if __name__ == '__main__':
    do_things()
