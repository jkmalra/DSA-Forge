import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        # multiple numbers
        multiply = math.prod(int(mul) for mul in str(n))
        print(multiply)
        
        # add numbers
        addition = sum(int(add) for add in str(n))
        print(addition)

        # minus both answers
        return multiply - addition