class Solution:
    def clearStars(self, s: str) -> str:
        hp = []
        arr = list(s)
        dc = {}

        for i in range(len(s)):
            c = s[i]
            if c != "*":
                heappush(hp, c)
                if c not in dc:
                    dc[c] = []
                dc[c].append(i)
            else:
                cc = heappop(hp)
                ii = dc[cc].pop()
                arr[ii] = ""
                arr[i] = ""

        return "".join(arr)
        