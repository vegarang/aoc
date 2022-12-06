from year2022.day05.stack import Supplies


def run_part_2(values):
    supplies = Supplies(values=values)
    supplies.perform_bulk_move_operations()
    print('part2: ')
    supplies.print_top_of_stacks()