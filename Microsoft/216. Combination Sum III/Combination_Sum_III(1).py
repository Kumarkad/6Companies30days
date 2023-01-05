class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        nums=[i for i in range(1,10)]

        combo=itertools.combinations(nums,k)

        return [c for c in combo if sum(c)==n]
