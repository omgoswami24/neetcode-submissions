class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for let in s:
            if let in letters:
                letters[let] += 1
            else:
                letters[let] = 1
        
        for let in t:
            if let in letters:
                letters[let] -= 1
            else:
                return False
        
        for key in letters:
            if letters[key] != 0:
                return False
        
        return True
        