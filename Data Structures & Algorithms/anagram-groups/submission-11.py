class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for s in strs:
            res = "".join(sorted(s))
            if res in groups:
                groups[res].append(s)
            else: groups[res] = [s]
        
        return list(groups.values())