class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        window = {}
        maxStringSize = 0
        currWindowLength = 0
        while right < len(s):
            
            if s[right] in window:
                window[s[right]] = window[s[right]] + 1
            else:
                window[s[right]] = 1
            right = right + 1

            while right-left > window[max(window, key = window.get)] + k:
                window[s[left]] -= 1
                left += 1
            maxStringSize = max(right-left, maxStringSize)
        return maxStringSize

        