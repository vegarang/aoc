from year2022.day02.shared import get_day_points


def get_part1_points(values):
    points = 0
    for value in values:
        value = value.strip()
        if value == '':
            continue
        other, me = value.split(' ')
        points += get_day_points(other, me)
    return points

