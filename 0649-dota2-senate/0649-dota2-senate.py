class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad, dire = deque(), deque()

        for i in range(len(senate)):
            if senate[i]=="R":
                rad.append(i)
            else: dire.append(i)
        
        curr = len(senate)

        while rad and dire:
            r, d = rad.popleft(), dire.popleft()
            if r<d:
                rad.append(curr)
            else:
                dire.append(curr)
            curr+=1
        if dire:
            return "Dire"
        else: return "Radiant"


        