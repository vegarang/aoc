from year2022.day08.TreeGrid import GRID, make_grid


def load_file():
    with open('input.txt', 'r') as f:
        values = f.readlines()
    return values


def count_visible_trees():
    count = 0
    for y in range(0, len(GRID)):
        for x in range(0, len(GRID[y])):
            # visible = False
            if GRID[y][x].is_visible():
                # visible = True
                count += 1
            # print(f'{GRID[y][x].get_value()}:{"y" if visible else "n"}', end=' ')
        # print()

    return count


def get_highest_scenic_score():
    highest = 0
    for y in range(0, len(GRID)):
        for x in range(0, len(GRID[y])):
            # visible = False
            score = GRID[y][x].calculate_scenic_score()
            if score > highest:
                highest = score
    return highest


def do_things():
    values = load_file()
    make_grid(lines=values)

    visible_trees = count_visible_trees()
    print(f'part1, visible trees: {visible_trees}')

    highest_scenic_score = get_highest_scenic_score()
    print(f'part2, highest score: {highest_scenic_score}')


if __name__ == '__main__':
    do_things()
