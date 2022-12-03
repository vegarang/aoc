import json

ASCII_OFFSET_LOWER = ord('a') - 1
ASCII_OFFSET_UPPER = ord('A') - 27


def char_to_pri(char):
    ascii_value = ord(char)
    if char.islower():
        return ascii_value - ASCII_OFFSET_LOWER
    return ascii_value - ASCII_OFFSET_UPPER


class Rucksack:
    def __init__(self, values):
        self.plain_values = values.strip()
        self.small_compartment = []
        self.large_compartment = []
        self.populate_compartments()

    def populate_compartments(self):
        length = len(self.plain_values)
        per_compartment = length / 2
        count = 0
        for character in self.plain_values:
            if count < per_compartment:
                self.small_compartment.append(character)
            else:
                self.large_compartment.append(character)
            count += 1

    def get_shared_items(self):
        small_set = set(self.small_compartment)
        large_set = set(self.large_compartment)
        intersection = small_set & large_set
        return intersection

    def get_shared_item_priorities(self):
        priorities = []
        summed_priorities = 0
        for shared in self.get_shared_items():
            priority = char_to_pri(shared)
            priorities.append(priority)
            summed_priorities += priority
        return summed_priorities, priorities

    def get_all_unique_items(self):
        return set(self.small_compartment) | set(self.large_compartment)


def make_rucksacks(values):
    rucksacks = []
    for value in values:
        rucksacks.append(Rucksack(value))
    return rucksacks
