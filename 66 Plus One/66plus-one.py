class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if (digits[-1]) < 9 :
            digits[-1] +=1
            return digits
        ret = 0
        for i in digits:
            ret += i
            ret *= 10
        ret //= 10
        ret +=1
        # print(ret)
        c = ret
        cnt = 0
        while (ret > 0):
            cnt += 1
            ret//=10
        ans = [0 for i in range(cnt)]
        i = cnt-1
        for i in range(i, -1 , -1):
            ans[i] = c %10
            c //= 10
        return ans


            

            
        