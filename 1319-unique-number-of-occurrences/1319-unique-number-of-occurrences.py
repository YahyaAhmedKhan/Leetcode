class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dc = {}
        for v in arr:
            if v not in dc:
                dc[v] = 0
            dc[v] +=1
        
        st = set()
        for val in list(dc.values()):
            if val not in st: st.add(val)
            else: return False

        return True