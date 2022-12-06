from year2022.day05.stack import Supplies


def run_part_1(values):
    supplies = Supplies(values=values)
    supplies.perform_move_operations_one_by_one()
    print('part1: ')
    supplies.print_top_of_stacks()