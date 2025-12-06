class Solution:
    def completePrime(self, num: int) -> bool:
        def  is_prime(n):
            if n<2:
                return False
            if n % 2 == 0:
                return n == 2

            r = int(n ** 0.5)
            for i in range(3, r +1, 2):
                if n % i == 0:
                    return False
            return True
        
        s = str(num)
        cash = {}
            
        for k in range(1, len(s) + 1):
            for v in (int(s[:k]), int(s[-k:])):
                if v not in cash:
                    cash[v] = is_prime(v)
                if not cash[v]:
                    return False
                    
        return True
    

# Complete Prime Number
# Medium
# 4 pt.
# You are given an integer num.

# A number num is called a Complete Prime Number if every prefix and every suffix of num is prime.

# Return true if num is a Complete Prime Number, otherwise return false.

# Note:

# A prefix of a number is formed by the first k digits of the number.
# A suffix of a number is formed by the last k digits of the number.
# A prime number is a natural number greater than 1 with only two factors, 1 and itself.
# Single-digit numbers are considered Complete Prime Numbers only if they are prime.
#  

# Example 1:

# Input: num = 23

# Output: true

# Explanation:

# ​​​​​​​Prefixes of num = 23 are 2 and 23, both are prime.
# Suffixes of num = 23 are 3 and 23, both are prime.
# All prefixes and suffixes are prime, so 23 is a Complete Prime Number and the answer is true.
# Example 2:

# Input: num = 39

# Output: false

# Explanation:

# Prefixes of num = 39 are 3 and 39. 3 is prime, but 39 is not prime.
# Suffixes of num = 39 are 9 and 39. Both 9 and 39 are not prime.
# At least one prefix or suffix is not prime, so 39 is not a Complete Prime Number and the answer is false.
# Example 3:

# Input: num = 7

# Output: true

# Explanation:

# 7 is prime, so all its prefixes and suffixes are prime and the answer is true.
#  

# Constraints:

# 1 <= num <= 109