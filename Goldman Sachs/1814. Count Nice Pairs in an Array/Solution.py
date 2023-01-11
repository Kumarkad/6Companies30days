class Solution:

    def countNicePairs(self, nums: List[int]) -> int:

        res = 0 

        count = Counter() 

        for a in nums:

            b = int(str(a)[::-1])

            res += count[a - b] 

            count[a - b] += 1 

        return res % (10**9 + 7)
