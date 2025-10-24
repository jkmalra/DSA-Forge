class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1:
            return word  # no cuts, whole string appears
        
        max_len = n - numFriends + 1
        best = ""
        for i in range(n):
            candidate = word[i:i + max_len]
            if candidate > best:
                best = candidate
        return best


# Test Cases
print(Solution().answerString("dbca", 2))  # "dbc"
print(Solution().answerString("gggg", 4))  # "g"
print(Solution().answerString("aann", 2))  # "nn"
print(Solution().answerString("gh", 1))    # "gh"
print(Solution().answerString("abcdef", 3))# "def"