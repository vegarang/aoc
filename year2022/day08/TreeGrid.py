GRID = []


def make_grid(lines):
    y = 0
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        GRID.append([])
        x = 0
        for char in line:
            GRID[y].append(Tree(x=x, y=y, value=char))
            x += 1
        y += 1


class Tree:
    def __init__(self, x, y, value):
        self._x = int(x)
        self._y = int(y)
        self._value = int(value)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_value(self):
        return self._value

    def is_visible(self):
        if self._x == 0 or self._x == len(GRID[self._y]) - 1 or self._y == 0 or self._y == len(GRID) - 1:
            return True

        max_height = self._value
        visible_before_x = True
        visible_before_y = True
        visible_after_x = True
        visible_after_y = True

        for before_x in range(0, self._x):
            if GRID[self._y][before_x].get_value() >= max_height:
                visible_before_x = False

        for after_x in range(self._x + 1, len(GRID[self._y])):
            if GRID[self._y][after_x].get_value() >= max_height:
                visible_after_x = False

        for before_y in range(0, self._y):
            if GRID[before_y][self._x].get_value() >= max_height:
                visible_before_y = False

        for after_y in range(self._y + 1, len(GRID)):
            if GRID[after_y][self._x].get_value() >= max_height:
                visible_after_y = False

        return visible_before_x or visible_before_y or visible_after_x or visible_after_y

    def calculate_scenic_score(self):
        left_count = 1 if self._x == 0 else 0
        right_count = 1 if self._x == len(GRID[self._y]) - 1 else 0
        up_count = 1 if self._y == 0 else 0
        down_count = 1 if self._y == len(GRID) - 1 else 0

        index = self._x - 1
        while index >= 0:
            left_count += 1
            if GRID[self._y][index].get_value() >= self._value:
                break
            index -= 1

        index = self._x + 1
        while index < len(GRID[self._y]):
            right_count += 1
            if GRID[self._y][index].get_value() >= self._value:
                break
            index += 1

        index = self._y - 1
        while index >= 0:
            up_count += 1
            if GRID[index][self._x].get_value() >= self._value:
                break
            index -= 1

        index = self._y + 1
        while index < len(GRID):
            down_count += 1
            if GRID[index][self._x].get_value() >= self._value:
                break
            index += 1

        return left_count * right_count * up_count * down_count
