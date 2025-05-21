class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix[0]), len(matrix)
        st = set()
        def setZero(row, col):
            for i in range(n):
                # matrix[row][i]
                st.add((row, i))

            for j in range(m):
                # matrix[j][col] = 0
                st.add((j, col))

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    setZero(i, j)
        for i, j in list(st):
            matrix[i][j] = 0
        # return matrix
        