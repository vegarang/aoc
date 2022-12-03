from year2022.day03.shared import char_to_pri, make_rucksacks


def run_part_2(values):
    rucksacks = make_rucksacks(values)
    unique_items = []
    summed_priorities = 0
    for rucksack in rucksacks:
        unique_items.append(rucksack.get_all_unique_items())
        if len(unique_items) == 3:
            result = list(unique_items[0] & unique_items[1] & unique_items[2])
            if len(result) != 1:
                raise Exception('More than one item in common between elves!')
            summed_priorities += char_to_pri(result[0])
            unique_items = []

    print('Part 2 total: ', summed_priorities)
