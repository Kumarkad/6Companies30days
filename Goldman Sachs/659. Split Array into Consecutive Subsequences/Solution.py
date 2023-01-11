class Solution:

    def isPossible(self, nums: List[int]) -> bool:

        left = Counter(nums)

        right= Counter() 

        for i in nums: 

            if not left[i]: continue 

            left[i] -= 1

            if right[i - 1] > 0: 

                right[i - 1] -= 1 

                right[i] += 1 

            elif left[i + 1] and left[i + 2]: 

                left[i + 1] -= 1 

                left[i + 2] -= 1 

                right[i + 2] += 1

            else: 

                return False 

        return True
