class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort all of them -> O(n)

        seen = {}
        final = []

        for str in strs:
            temp = "".join(sorted(str))

            if temp in seen:
                seen[temp].append(str)
            else:
                seen[temp] = [str]
        
        final = []

        for key,value in seen.items():
            final.append(value)

        return final
            

        
        