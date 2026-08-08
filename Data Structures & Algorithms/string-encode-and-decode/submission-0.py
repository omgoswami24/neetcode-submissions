class Solution:

    def encode(self, strs: List[str]) -> str:
        size = 0
        result = ''
        for s in strs:
            result += str(len(s))
            result += "#"
            result += s
        return result


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1

            size = int(s[i:j])
            i = j + 1
            j = i + size
            result.append(s[i:j])
            i = j
            
            

        return result

