from year2022.day04.utils.range import Range


class Pair:
    def __init__(self, plain_values):
        ranges = plain_values.strip().split(',', maxsplit=1)
        self.range1 = Range(values=ranges[0])
        self.range2 = Range(values=ranges[1])

    def one_contains_other(self) -> bool:
        return self.range1.fully_contains(self.range2) or self.range1.fully_contained_by(self.range2)

    def ranges_overlap(self) -> bool:
        return self.range1.overlaps_with(self.range2)
