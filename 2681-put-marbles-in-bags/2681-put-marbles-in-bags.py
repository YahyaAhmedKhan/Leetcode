class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        pairs = [0] * (len(weights)-1)

        for i in range(len(weights)-1):
            pairs[i] = weights[i] + weights[i+1]

        pairs.sort()
        mini = weights[0] + weights[-1]
        maxi = weights[0] + weights[-1]

        mini += sum(pairs[:k-1])
        pairs.reverse()
        maxi += sum(pairs[:k-1])
        return maxi-mini


        