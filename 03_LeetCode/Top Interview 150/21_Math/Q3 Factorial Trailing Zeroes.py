class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n = n // 5
            count += n
        return count
    
# x = 5 // 5
# print(x)

# x = 3 // 5
# print(x)