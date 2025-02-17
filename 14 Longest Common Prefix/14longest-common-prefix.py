class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr_char = ''
        ans = ""
        m = min([len(s) for s in strs])
        for i in range(m):
            curr = strs[0][i]
            for s in strs:
                if s[i] != curr:
                    return ans
            ans += curr
        return ans