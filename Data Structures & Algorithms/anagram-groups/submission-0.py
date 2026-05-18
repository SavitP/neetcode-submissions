class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        toReturn = []
        for word in strs:
            found = False
            for i in range (len(toReturn)):
                if ("".join(sorted(word)) == "".join(sorted(toReturn[i][0]))):
                    toReturn[i].append(word)
                    found = True
            if not found:
                toReturn.append([word])
        return toReturn