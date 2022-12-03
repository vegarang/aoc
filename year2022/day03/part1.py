from year2022.day03.shared import make_rucksacks


def run_part_1(values):
    rucksacks = make_rucksacks(values)
    total = 0
    for rucksack in rucksacks:
        summed_priorities, items = rucksack.get_shared_item_priorities()
        total += summed_priorities

    print(f'Part 1 total: {total}')
