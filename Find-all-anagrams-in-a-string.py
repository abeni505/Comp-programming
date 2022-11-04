class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        result, prefix, check = [], {}, {}
        for i in range(len(p)):  prefix[p[i]] = 1 + prefix.get(p[i], 0)
        for i in range(len(p) - 1): check[s[i]] = 1 + check.get(s[i], 0)
        x, y = 0, len(p) - 1
        while y < len(s):
            check[s[y]] = 1 + check.get(s[y], 0)
            if check == prefix: result.append(x)
            check[s[x]] -= 1
            if check[s[x]] == 0: check.pop(s[x])
            x, y = x + 1, y + 1
        return result
