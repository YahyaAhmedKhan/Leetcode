class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        if not s:
            return 0
        l = 0
        ans = 1
        for r in range(len(s)):
            if s[r] not in st:
                st.add(s[r])
                ans = max(ans, r-l+1)
            else:
                while s[r] in st:
                    st.remove(s[l])
                    l+=1
                st.add(s[r])
        return ans

        