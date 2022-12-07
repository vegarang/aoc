class PathObject:
    children = None

    def __init__(self, parent, name, dir_or_file):
        self.parent = parent
        self.name = name
        self.type = dir_or_file

    def is_dir(self):
        return self.type == 'dir'

    def is_file(self):
        return self.type == 'file'

    def is_root(self):
        return self.parent is None

    def get_full_path(self):
        if self.is_root():
            return '/'

        return f'{self.parent.get_full_path()}{self.name}{"/" if self.is_dir() else ""}'

    def get_file_tree_indents(self):
        node = self
        indent = 0
        while node.parent is not None:
            node = node.parent
            indent += 2
        return indent

    def get_file_tree_descriptor(self):
        raise NotImplementedError()

    def print_file_tree(self):
        print(f'{" " * self.get_file_tree_indents()}- {self.name} {self.get_file_tree_descriptor()}')
        if self.children is not None:
            for child in self.children.values():
                child.print_file_tree()

    def get_size(self, register_in_object=None):
        raise NotImplementedError()


class Directory(PathObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, dir_or_file='dir')
        self.children = {}

    def add_file(self, name, size):
        self.children[name] = File(parent=self, name=name, size=size)

    def add_dir(self, name):
        self.children[name] = Directory(parent=self, name=name)

    def get_child_dir(self, name):
        child = self.children.get(name, None)
        if child is None:
            raise Exception(f'child directory not found: {name}, current: {self.name}')
        if not child.is_dir():
            raise Exception(f'{name} is not a directory!')
        return child

    def get_file_tree_descriptor(self):
        return '(dir)'

    def get_size(self, register_in_object=None):
        total_size = 0
        for child in self.children.values():
            total_size += child.get_size(register_in_object=register_in_object)
            if register_in_object is not None:
                register_in_object[self.get_full_path()] = total_size
        return total_size


class File(PathObject):
    def __init__(self, size, *args, **kwargs):
        super().__init__(*args, **kwargs, dir_or_file='file')
        self.size = size

    def get_file_tree_descriptor(self):
        return f'(file, size={self.size})'

    def get_size(self, *args, **kwargs):
        return int(self.size)
