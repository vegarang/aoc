def is_rock(value) -> bool:
    return value in ['A', 'X']


def is_paper(value) -> bool:
    return value in ['B', 'Y']


def is_scissors(value) -> bool:
    return value in ['C', 'Z']


def is_win(other, me) -> bool:
    if is_rock(other) and is_paper(me):
        return True
    if is_paper(other) and is_scissors(me):
        return True
    if is_scissors(other) and is_rock(me):
        return True
    return False


def is_draw(other, me) -> bool:
    if is_rock(other) and is_rock(me):
        return True
    if is_paper(other) and is_paper(me):
        return True
    if is_scissors(other) and is_scissors(me):
        return True


def is_loss(other, me) -> bool:
    if is_rock(other) and is_scissors(me):
        return True
    if is_paper(other) and is_rock(me):
        return True
    if is_scissors(other) and is_paper(me):
        return True
    return False


def get_shape_point(me) -> int:
    if is_rock(me):
        return 1
    if is_paper(me):
        return 2
    if is_scissors(me):
        return 3
    raise Exception(f'Cannot get shape point for invalid shape: {me}')


def get_result_point(other, me) -> int:
    if is_win(other, me):
        return 6
    if is_draw(other, me):
        return 3
    if is_loss(other, me):
        return 0
    raise Exception(f'Cannot get result point when neither win, draw or loss. Got other: {other} and me: {me}')


def get_day_points(other, me) -> int:
    shape_point = get_shape_point(me)
    result_point = get_result_point(other, me)
    return shape_point + result_point
