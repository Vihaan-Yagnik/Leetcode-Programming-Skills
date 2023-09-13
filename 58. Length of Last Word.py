class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ok = s.split()
        return len(ok[-1])
