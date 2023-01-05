class Solution:

    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:

        g = gcd(*numsDivide)

        small = min((a for a in nums if g % a == 0), default = 0) 

        return sum(a < small for a in nums) if small else -1
