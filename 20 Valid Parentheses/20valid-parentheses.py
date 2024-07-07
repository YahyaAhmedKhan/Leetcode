class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        l = set(['(', '{', '['])
        r = set([')', '}', ']'])
        map = {")" : "(", "}": "{", "]":"["}
        for i in s:
            if i in l:
                arr.append(i)
            elif i in r:
                if (len(arr) == 0):
                    return False
                if arr[-1] == map[i]:
                    arr.pop()
                else:
                    return False
        return (len(arr) ==0)

