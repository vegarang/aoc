def load_file():
    with open('input.txt', 'r') as f:
        values = f.readlines()
    return values


def do_things():
    values = load_file()


if __name__ == '__main__':
    do_things()