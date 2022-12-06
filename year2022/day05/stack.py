import json
import re
from collections import OrderedDict


class Supplies:
    def __init__(self, values):
        self.values = values
        self.stacks = OrderedDict(
            [
                ('1', []),
                ('2', []),
                ('3', []),
                ('4', []),
                ('5', []),
                ('6', []),
                ('7', []),
                ('8', []),
                ('9', [])
            ]
        )
        self.total_move_operations = 0
        self.initialize_stacks()

    def append_to_stack(self, stack_index, value, first=False):
        stack_index = f'{stack_index}'
        if first:
            self.stacks[stack_index].insert(0, value)
        else:
            self.stacks[stack_index].append(value)

    def get_from_stack(self, stack_index):
        stack_index = f'{stack_index}'
        return self.stacks[stack_index].pop()

    def shift_from_stack(self, from_stack, to_stack):
        self.append_to_stack(stack_index=to_stack, value=self.get_from_stack(from_stack))

    def move_from_stack(self, from_stack, to_stack, number):
        from_stack_index = f'{from_stack}'
        to_stack_index = f'{to_stack}'
        tmp = self.stacks[from_stack_index]
        offset = len(tmp) - int(number)
        new_from = tmp[:offset]
        items_to_move = tmp[offset:]
        self.stacks[from_stack_index] = new_from
        self.stacks[to_stack_index].extend(items_to_move)

    def initialize_stacks(self):
        for value in self.values:
            if value.strip() == '':
                break
            stack_values = re.findall('.{1,4}', value)
            for i in range(0, len(stack_values)):
                stack_value = stack_values[i].strip()
                if stack_value == '':
                    continue
                stack_index = f'{i + 1}'
                if len(stack_value) == 1:
                    continue
                self.append_to_stack(stack_index=stack_index, value=stack_value[1], first=True)

    def perform_for_each_move_entry(self, operation):
        exp = re.compile(r'^move (?P<num>\d+) from (?P<from>\d+) to (?P<to>\d+)\s*$')
        for value in self.values:
            match = exp.fullmatch(value)
            if match is None:
                continue
            num_shifts = match.group('num')
            from_stack = match.group('from')
            to_stack = match.group('to')
            operation(number=num_shifts, from_stack=from_stack, to_stack=to_stack)

    def perform_move_operations_one_by_one(self):
        def _move_one_by_one(number, from_stack, to_stack):
            for i in range(0, int(number)):
                self.total_move_operations += 1
                self.shift_from_stack(from_stack=from_stack, to_stack=to_stack)
        self.perform_for_each_move_entry(_move_one_by_one)

    def perform_bulk_move_operations(self):
        self.perform_for_each_move_entry(self.move_from_stack)

    def print_top_of_stacks(self):
        sorted_keys = sorted(iter(self.stacks))
        for stack_index in sorted_keys:
            stack = self.stacks[stack_index]
            print(f'{stack[len(stack) - 1]}', end="")
        print()
