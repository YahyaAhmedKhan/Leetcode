class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for left in asteroids:
            if len(st)==0:
                st.append(left)
            elif left > 0:
                st.append(left)
            else:
                st.append(left)
                while(len(st)>1):
                    b, a = st.pop(), st.pop()
                    if a < 0:
                        st.append(a)
                        st.append(b)
                        break
                    if a == abs(b):
                        break
                    elif a>abs(b):
                        st.append(a)
                        break
                    else:
                        st.append(b)

        return st