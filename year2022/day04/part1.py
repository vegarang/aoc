from year2022.day04.utils import Pair


def run_part_1(values):
    fully_contained_ranges = 0
    for value in values:
        if value.strip() == '':
            continue
        pair = Pair(value)
        if pair.one_contains_other():
            fully_contained_ranges += 1

    print(f'Part1 - Fully contained ranges: {fully_contained_ranges}')
