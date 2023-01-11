class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator % denominator == 0:

            return str(numerator // denominator)

        p, q = map(abs, (numerator, denominator)) 

        prefix = ('' if (numerator > 0) == (denominator > 0) else '-') + str(p // q) + '.'

        suffix = ''

        remainder = p % q 

        index = {}

        while remainder not in index:

            index[remainder] = len(suffix) 

            suffix += str(remainder * 10 // q) 

            remainder = remainder * 10 % q 

            if remainder == 0: return prefix + suffix

        return prefix + suffix[:index[remainder]] + '(' + suffix[index[remainder]:] + ')'
