def all_unique(values):
    char_set = [False] * 128
    for i in range(0, len(values)):
        val = ord(values[i])
        if char_set[val]:
            return False
        char_set[val] = True
    return True


def get_next_marker(values, marker_length):
    index = 0
    end_index = marker_length + index
    while end_index < len(values) and not all_unique(values[index:end_index]):
        index += 1
        end_index = marker_length + index

    return end_index
