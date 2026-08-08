class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())
        s = s.lower()

        alphanumeric = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        left = 0
        right = len(s) - 1

        while left < right:
            while (s[left] not in alphanumeric and left < right):
                left += 1

            while (s[right] not in alphanumeric and left < right):
                right -= 1

            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
        