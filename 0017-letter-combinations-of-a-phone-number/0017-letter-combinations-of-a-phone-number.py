class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr = []
        n = len(digits)
        if n==0:
            return []
        vals = [
            [],     # 0
            [],     # 1
            ["a", "b", "c"],       # 2
            ["d", "e", "f"],       # 3
            ["g", "h", "i"],       # 4
            ["j", "k", "l"],       # 5
            ["m", "n", "o"],       # 6
            ["p", "q", "r", "s"],  # 7
            ["t", "u", "v"],       # 8
            ["w", "x", "y", "z"]   # 9
        ]
        def addtostrings(i):
            if i==-1:
                return [""]

            prev = addtostrings(i-1)
            ans = []
            print(i, prev)
            for pre in prev:
                for letter in vals[int(digits[i])]:
                    newstr = pre+letter
                    ans.append(newstr)
            return ans

        return addtostrings(n-1) 

        
                
