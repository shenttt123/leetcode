class Solution:
    def longestCommonPrefix(strs: List[str]):
        shortest = len(min(strs, key=len))

        for stringindex in range(1, len(strs)):
            for charindex in range(shortest):
                if strs[0][charindex] != strs[stringindex][charindex]:
                    shortest=charindex
                    break
        return strs[0][:shortest]

        
        
