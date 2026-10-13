class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        if not strs:
            return ""


        first = strs[0]
        for i in range(len(first)):
            c = first[i]

            for j in range(1, len(strs)):

                if i >= len(strs[j]) or strs[j][i] != c:
                    return first[:i]
        return first