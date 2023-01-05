class Solution:

    def getHint(self, secret: str, guess: str) -> str:

        bulls = 0 

        sh = defaultdict(int) 

        gh = defaultdict(int)

        for s, g in zip(secret, guess): 

            if s == g: 

                bulls += 1

            else:

                sh[s] += 1 

                gh[g] += 1 

        cows = sum(min(sh[k], gh[k]) for k in sh) 

        return "{}A{}B".format(bulls, cows)
