class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def dfs(currsum, currk, curri, currstr):
            nonlocal n
            if currk<0:
                return
            
            for j in range(curri+1, 10):
                newstr = currstr+str(j)
                newsum = currsum+j
                if currk==1 and newsum==n:
                    arr = list(map(int, list(newstr)))
                    ans.append(arr)
                    break
                if newsum<n:
                    dfs(newsum, currk-1, j, newstr)
                elif newsum>n:
                    break
                
        dfs(0, k, 0, "")

        return ans




            

        