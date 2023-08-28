class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # folding the string in two equal parts
        s_fold = "".join( (s[1:], s[:-1]))
        # check if our main string is there in the fold
        return s in s_fold
