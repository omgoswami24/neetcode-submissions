class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        highest = len(nums)

        total = highest * (highest + 1) // 2

        actual = sum(nums)

        return total - actual


        