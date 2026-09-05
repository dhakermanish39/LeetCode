class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowel = 'aeiou'
        v, c = 0, 0
        for x in s:
            if x in vowel:
                v += 1
            elif x.isalpha():
                c += 1
        if c > 0:
            return v // c
        return 0
        