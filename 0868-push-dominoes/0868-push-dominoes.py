class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        doms = dominoes

        ans = ["."]*n
        pos = []
        for i in range(n):
            if doms[i]!=".":
                pos.append(i)
                ans[i] = doms[i]

        if not pos: return dominoes

        
        def handleRL(l, r):
            while l<r:
                ans[l] = "R"
                ans[r] = "L"
                l+=1
                r-=1

        p = len(pos)
        for pi in range(p-1):
            l, r = pos[pi], pos[pi+1]

            state = (doms[l], doms[r])
            print(state)
            if state == ("L", "L"):
                for i in range(l, r+1):
                    ans[i] = "L"
            elif state == ("R", "R"):
                for i in range(l, r+1):
                    ans[i] = "R"
            elif state == ("R","L"):
                handleRL(l, r)
                

        fr, sc = pos[0], pos[-1]
        if doms[fr] == "L":
            for i in range(fr):
                ans[i] = "L"
        if doms[sc] == "R":
            for i in range(sc, n):
                ans[i] = "R"


        return "".join(ans)
                

                
