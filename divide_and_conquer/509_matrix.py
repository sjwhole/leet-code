class Solution:
    def mul(self, a, b):
        ans = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    ans[i][j] += a[i][k] * b[k][j]
        return ans

    def square(self, matrix, n):
        if n == 1:
            return matrix
        if n % 2 == 0:
            return self.mul(self.square(matrix, n // 2), self.square(matrix, n // 2))
        else:
            return self.mul(self.mul(self.square(matrix, n // 2), self.square(matrix, n // 2)), matrix)

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        m = [[0, 1], [1, 1]]
        m = self.square(m, n)
        return m[0][1]
