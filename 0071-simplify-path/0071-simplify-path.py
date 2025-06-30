class Solution:
    def simplifyPath(self, path: str) -> str:
        comps = path.split("/")
        st = []


        for i in comps:
            if i == "" or i==".":
                continue
            elif i == "..":
                if st:
                    st.pop()
            else:
                st.append(i)

        return "/" + "/".join(st)
        