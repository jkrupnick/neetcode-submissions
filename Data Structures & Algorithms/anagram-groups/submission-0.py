class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for i in range(len(strs)):
            sortedStrs = "".join(sorted(strs[i]))
            if sortedStrs in anagrams:
                anagrams[sortedStrs].append(strs[i])
            else:
                anagrams[sortedStrs] = [strs[i]]
        return list(anagrams.values())
        


        