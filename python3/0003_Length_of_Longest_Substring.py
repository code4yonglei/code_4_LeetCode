class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        c = {}
        left, ans = 0, 1
        for right in range(n):
            if s[right] in c:
                left = max(left, c[s[right]] + 1)
            c[s[right]] = right
            ans = max(ans, right - left + 1)
        return ans


###################################

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter()
        left = ans = 0
        for right in range(len(s)):
            c[s[right]] += 1
            while c[s[right]] > 1:
                c[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


