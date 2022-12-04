class Range:
    def __init__(self, values):
        value_range = values.split('-', maxsplit=1)
        self.start = int(value_range[0])
        self.end = int(value_range[1])

    def fully_contains(self, other_range) -> bool:
        return self.start <= other_range.start and self.end >= other_range.end

    def fully_contained_by(self, other_range) -> bool:
        return self.start >= other_range.start and self.end <= other_range.end

    def overlaps_with(self, other_range) -> bool:
        other_start_in_self = self.start <= other_range.start <= self.end
        other_end_in_self = self.start <= other_range.end <= self.end
        return other_start_in_self or \
            other_end_in_self or \
            self.fully_contains(other_range) or \
            self.fully_contained_by(other_range)
