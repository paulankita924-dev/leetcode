class NumArray:

    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.bit = [0] * (self.n + 1)

        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def _add(self, index, delta):
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index

    def _prefix_sum(self, index):
        s = 0
        while index > 0:
            s += self.bit[index]
            index -= index & -index
        return s

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix_sum(right + 1) - self._prefix_sum(left)