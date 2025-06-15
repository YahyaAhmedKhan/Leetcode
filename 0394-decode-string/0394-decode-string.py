class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for c in s:
            if c == "]":
                ss = []
                while st[-1]!="[":
                    ss.append(st.pop())
                st.pop() # get rid of "["

                ss.reverse()
                ss = "".join(ss)
                number = []
                while len(st)>0 and st[-1].isdigit():
                    number.append(st.pop())
                number.reverse()
                number = int("".join(number))
                ret = ""
                for i in range(number):
                    ret += ss
                st.append(ret)
            else:
                st.append(c)

        return "".join(st)