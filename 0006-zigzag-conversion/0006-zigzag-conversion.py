class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = [0]* len(s)
        n = len(s)

        isIncr = True
        curr = 1
        for i in range(1, n):
            arr[i] = curr
            if curr in (numRows-1, 0):
                isIncr = not isIncr

            curr += 1 if isIncr else -1

        # print(arr)

        ans = [[] for i in range(numRows)]
        for i in range(n):
            ans[arr[i]].append(s[i])
        
        final = ""
        for seq in ans:
            part = "".join(seq)
            final += part
        return final


            
        