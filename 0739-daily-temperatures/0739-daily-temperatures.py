class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        hp = []
        temp = temperatures
        n = len(temp)
        ans = [0]*n
        for i in range(n):
            t = temp[i]

            while hp and hp[0][0]<t:
                smallt, previ = heappop(hp)
                ans[previ] = i-previ
            heappush(hp, (t, i))

        return ans
                






        