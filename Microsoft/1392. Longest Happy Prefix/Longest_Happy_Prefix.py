class Solution:

    def longestPrefix(self, s: str) -> str:

        n = len(s) 

        dfa = [0] * n 

        d = 0 

        for i in range(1, n):

            while d and s[d] != s[i]:

                d = dfa[d - 1] 

            d += s[i] == s[d] 

            dfa[i] = d 

        return s[:dfa[n - 1]]
