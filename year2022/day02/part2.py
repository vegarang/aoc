from year2022.day02.shared import get_day_points, is_rock, is_paper, is_scissors

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'


def calculate_todays_move(other, outcome) -> str:
    if is_rock(other):
        if outcome == LOSE:
            return SCISSORS
        if outcome == DRAW:
            return ROCK
        if outcome == WIN:
            return PAPER
    if is_paper(other):
        if outcome == LOSE:
            return ROCK
        if outcome == DRAW:
            return PAPER
        if outcome == WIN:
            return SCISSORS
    if is_scissors(other):
        if outcome == LOSE:
            return PAPER
        if outcome == DRAW:
            return SCISSORS
        if outcome == WIN:
            return ROCK


def get_part2_points(values) -> int:
    points = 0
    for value in values:
        value = value.strip()
        if value == '':
            continue
        other, outcome = value.split(' ')
        me = calculate_todays_move(other, outcome)
        points += get_day_points(other, me)
    return points
