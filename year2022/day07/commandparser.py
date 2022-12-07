from year2022.day07.directory import Directory

ROOT = Directory(name='/', parent=None)


class Parser:
    current_dir = ROOT

    def __init__(self, commands):
        self.commands = commands

    def change_dir(self, to):
        if to == '..':
            self.current_dir = self.current_dir.parent
        elif to == '/':
            self.current_dir = ROOT
        else:
            self.current_dir = self.current_dir.get_child_dir(name=to)

    def add_children(self, index):
        command = self.commands[index].strip()
        while not command.startswith('$') and command != '':
            command_fragments = command.split(' ')
            if command_fragments[0] == 'dir':
                self.current_dir.add_dir(name=command_fragments[1])
            else:
                self.current_dir.add_file(size=int(command_fragments[0]), name=command_fragments[1])

            index += 1
            command = self.commands[index].strip()

        return index

    def parse_commands(self):
        command_index = 0
        while command_index < len(self.commands):
            command = self.commands[command_index].strip()
            if command == '':
                command_index += 1
                continue
            if not command.startswith('$'):
                raise Exception(f'Not a command: {command}')

            command = command.lstrip('$ ').split(sep=' ')
            if command[0] == 'cd':
                self.change_dir(to=command[1])
                command_index += 1
            elif command[0] == 'ls':
                command_index = self.add_children(command_index + 1)
            else:
                raise Exception(f'Unknown command: {command[0]}')

