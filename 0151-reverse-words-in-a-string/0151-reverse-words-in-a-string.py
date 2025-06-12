class Solution:
    def reverseWords(self, s: str) -> str:
        
        curr = ""
        words = []
        for i in range(len(s)):
            if s[i] == " ":
                if len(curr)>0:
                    words.append(curr)
                curr = ""
            else: curr+=s[i]
        if len(curr)>0:
            words.append(curr)

        words.reverse()
        
        return " ".join(words)
            

        