class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1: return 'a'
        temp = 1 
        while temp<k:
            temp *=2
        print(temp)
        def helper(i, length):
            if i==0:
                return 0
            div = length//2
            if i < div:
                return helper(i, div)
            else:
                return 1 + helper(i%div, div)
        ans = helper(k-1, temp)
        return chr(ord('a')+ans)

        print(helper(k-1, temp))
        #     if
        