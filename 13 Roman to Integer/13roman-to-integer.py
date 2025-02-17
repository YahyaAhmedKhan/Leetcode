class Solution:
    def romanToInt(self, s: str) -> int:
        rom = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        n = 0
        for i in range(len(s)-1):
            su = rom[s[i]]
            su = (su * (-1 if rom[s[i]] < rom[s[i+1]] else 1))
            n += su
        n += rom[s[-1]]
        return n





        