class Solution:
    def reverseVowels(self, s: str) -> str:
        st = deque()
        arr = list(s)
        v = set(["a", "e", "i", "o", "u"])
        for c in arr:
            if c.lower() in v:
                st.append(c)
            
        for i in range(len(s)-1,-1,-1 ):
            if arr[i].lower() in v:
                arr[i] = st.popleft()

        return "".join(arr)


        