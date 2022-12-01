def load_file():
    file = open('input.txt', 'r')
    values = file.readlines()
    return values


def do_things():
    values = load_file()


if __name__ == '__main__':
    do_things()