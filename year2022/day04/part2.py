from year2022.day04.utils import Pair


def run_part_2(values):
    overlapping_ranges = 0
    for value in values:
        if value.strip() == '':
            continue
        pair = Pair(value)
        if pair.ranges_overlap():
            overlapping_ranges += 1

    print(f'Part2 - Overlapping ranges: {overlapping_ranges}')