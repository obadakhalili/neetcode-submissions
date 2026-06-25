class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = [char.lower() for char in s if char.isalnum()]
        for i in range(len(normalized)//2):
            if normalized[i] != normalized[-(i+1)]: return False
        return True