    if x < 0:
                return False
            num = x
            palindrome_number = 0
            while num > 0:
                last_digit = num % 10
                palindrome_number = (palindrome_number * 10) + last_digit
                num //= 10
                
            return palindrome_number == x


# TEST CASES:
# 121
# -121 = False
# 10 = False