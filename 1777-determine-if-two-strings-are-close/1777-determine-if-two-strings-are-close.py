class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!= len(word2): return False
        dc1 = {}
        dc2 = {}

        for a,b in zip(word1, word2):
            if a not in dc1:
                dc1[a] = 0
            if b not in dc2:
                dc2[b] = 0

            dc1[a] +=1
            dc2[b] +=1
        
        t1 = tuple(set(sorted(word1)))
        t2 = tuple(set(sorted(word2)))
        if t1!=t2: return False
        
        f1, f2 = {}, {}
        for val in list(dc1.values()):
            if val not in f1:
                f1[val ] =0
            f1[val] +=1
        
        for val in list(dc2.values()):
            if val not in f2:
                f2[val] = 0
            f2[val] +=1



        for key in f1:
            if (key not in f2): return False
            if f1[key]!=f2[key]: return False

        return True