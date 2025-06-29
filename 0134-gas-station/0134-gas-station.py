class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        arr = [a-b for a, b in zip(gas, cost)]
        if sum(cost)>sum(gas):return -1

        def trav(i):
            fuel = 0
            temp = i

            while fuel>=0:
                fuel += arr[i]
                i+=1
                i%=len(gas)
                if i==temp or fuel<0:
                    return i

        print(arr)
        i = 0
        while trav(i) > i:
            i = trav(i)
        if trav(i)==i:
            return i


