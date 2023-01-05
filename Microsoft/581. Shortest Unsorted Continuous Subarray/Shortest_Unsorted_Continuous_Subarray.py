class Solution:

    def findUnsortedSubarray(self, nums: List[int]) -> int:

        res = [i for (i, (a, b)) in enumerate(zip(nums, sorted(nums))) if a != b] 

        return 0 if not res else res[-1] - res[0] + 1
