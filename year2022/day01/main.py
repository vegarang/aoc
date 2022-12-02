
def load_file():
    with open('input.txt', 'r') as f:
        values = f.readlines()
    return values


def calculate_elfs(values):
    elfs = []
    index = 0
    for value in values:
        value = value.strip()
        if value == '':
            index += 1
            continue
        value = int(value)
        if len(elfs) < index + 1:
            elfs.append(value)
            continue
        elfs[index] += value
    return elfs


def find_largest_elf():
    values = load_file()
    elfs = calculate_elfs(values=values)
    sorted_elfs = sorted(elfs, reverse=True)
    first = sorted_elfs[0]
    second = sorted_elfs[1]
    third = sorted_elfs[2]
    total = first + second + third
    print(f'first: {first}\nsecond: {second}\nthird: {third}\ntotal: {total}')


if __name__ == '__main__':
    find_largest_elf()
