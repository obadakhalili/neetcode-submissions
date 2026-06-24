class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = dict()
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1
        for c in t:
            if c not in char_count:
                return False
            char_count[c] -= 1
        for v in char_count.values():
            if v != 0: return False
        return True