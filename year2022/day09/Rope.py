class RopeNode:
    def __init__(self, rope, parent_node=None, identifier=None):
        self.x = 0
        self.y = 0
        self.parent_node = parent_node
        self.child_node = None
        self.visited_locations = {'0,0'}
        self.identifier = identifier
        self.rope = rope

    def follow(self, other_node):
        x_diff = other_node.x - self.x
        y_diff = other_node.y - self.y

        new_x = self.x
        new_y = self.y

        def y_for_x(y):
            if y_diff >= 1:
                y = self.y + 1
            if y_diff <= -1:
                y = self.y - 1
            return y

        def x_for_y(x):
            if x_diff >= 1:
                x = self.x + 1
            if x_diff <= -1:
                x = self.x - 1
            return x

        if x_diff == 2:
            new_x = self.x + 1
            new_y = y_for_x(new_y)
        elif x_diff == -2:
            new_x = self.x - 1
            new_y = y_for_x(new_y)
        elif y_diff == 2:
            new_y = self.y + 1
            new_x = x_for_y(new_x)
        elif y_diff == -2:
            new_y = self.y - 1
            new_x = x_for_y(new_x)
        else:
            return
        self.x = new_x
        self.y = new_y

        self.visited_locations.add(f'{self.x},{self.y}')

    def follow_parent(self):
        self.follow(other_node=self.parent_node)
        if self.child_node is not None:
            self.child_node.follow_parent()

    def move(self, direction, times):
        if direction == 'U':
            field = 'y'
            amount = -1
        elif direction == 'D':
            field = 'y'
            amount = 1
        elif direction == 'L':
            field = 'x'
            amount = -1
        elif direction == 'R':
            field = 'x'
            amount = 1
        else:
            raise Exception(f'unknown direction: ', direction)

        while times >= 1:

            if field == 'x':
                self.x = self.x + amount
            elif field == 'y':
                self.y = self.y + amount

            if self.child_node is not None:
                self.child_node.follow_parent()

            times -= 1


class Rope:
    def __init__(self, number_of_knots):
        self.head = RopeNode(identifier='H', rope=self)
        self.tail = None
        prev_node = self.head

        for i in range(1, number_of_knots):
            node = RopeNode(parent_node=prev_node, rope=self)
            prev_node.child_node = node
            node.identifier = i
            if node.identifier == number_of_knots - 1:
                self.tail = node
            prev_node = node

    def handle_moves(self, moves):
        for move in moves:
            move = move.strip()
            if move == '':
                continue
            direction, times = move.split(' ')
            self.head.move(direction=direction, times=int(times))

    def get_unique_tail_positions(self) -> int:
        return len(self.tail.visited_locations)

    def print_node_grid(self):
        grid = []
        for y in range(0, 21):
            row = []
            for x in range(0, 26):
                row.append('.')
            grid.append(row)
        print()

        node = self.head
        grid[node.y][node.x] = f'{node.identifier}'
        while node.child_node is not None:
            node = node.child_node
            grid[node.y][node.x] = f'{node.identifier}'

        for row in grid:
            print(''.join(row))
