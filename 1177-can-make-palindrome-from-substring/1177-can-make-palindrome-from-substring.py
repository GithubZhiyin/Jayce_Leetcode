class Solution:
    def canMakePaliQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        memo = {}

        c = [[0] * 26 for _ in range(len(s) + 1)]
        for i in range(0, len(c)-1):
            for j in range(26):
                c[i + 1][j] = c[i][j]
            pos = ord(s[i]) - ord('a')
            c[i + 1][pos] += 1
        
        ans = []

        def pair_count(l, r):
            pair = 0
            for j in range(26):
                pair += (c[r + 1][j] - c[l][j]) // 2
            return pair 

        for query in queries:
            if (query[0], query[1]) in memo:
                pair = memo[(query[0], query[1])]
            else:
                pair = pair_count(query[0], query[1])
                memo[(query[0], query[1])] = pair

            length = query[1] - query[0] + 1
            pair_length = pair * 2 + min(length - pair * 2, query[2] * 2)
            if length % 2 == 0:
                ans.append(pair_length >= length)
            elif length % 2 == 1:
                ans.append(pair_length + 1 >= length)
        
        return ans 

            

                
            