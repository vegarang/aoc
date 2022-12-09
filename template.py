def load_file():
    with open('test_input.txt', 'r') as f:
        values = f.readlines()
    return values


def run_part_1(values):
    result = ''
    for value in values:
        pass

    print(f'part1: {result}')


def run_part_2(values):
    result = ''
    for value in values:
        pass

    print(f'part2: {result}')


def do_things():
    values = load_file()
    run_part_1(values=values)
    run_part_2(values=values)


if __name__ == '__main__':
    do_things()
