class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) -1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -=1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

# TEST CASES-----------------------------------------
if __name__ == "__main__":
    sol = ValidPalindrome()
    test_str = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(test_str)) # TRUE

    test_str2 = "race a car"
    print(sol.isPalindrome(test_str2)) # FALSE
