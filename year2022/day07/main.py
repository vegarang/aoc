import json

from year2022.day07.commandparser import Parser, ROOT


def load_file():
    with open('input.txt', 'r') as f:
        values = f.readlines()
    return values


def get_total_sizes() -> dict:
    total_sizes = {}
    ROOT.get_size(register_in_object=total_sizes)
    return total_sizes


def run_part_1():
    total_size = 0
    for size in get_total_sizes().values():
        if size >= 100_000:
            continue
        total_size += int(size)

    print(f'part1 sum of sizes: {total_size}')


def get_delete_size():
    device_size = 70_000_000
    needed_size = 30_000_000
    root_size = ROOT.get_size()
    free_size = device_size - root_size
    return needed_size - free_size


def run_part_2():
    limit = get_delete_size()
    smallest_size = None
    for size in get_total_sizes().values():
        if size >= limit and (smallest_size is None or smallest_size > size):
            smallest_size = size
    print(f'part2 size of smallest dir to delete: {smallest_size}')


def do_things():
    values = load_file()
    parser = Parser(commands=values)
    parser.parse_commands()

    run_part_1()
    run_part_2()


if __name__ == '__main__':
    do_things()
