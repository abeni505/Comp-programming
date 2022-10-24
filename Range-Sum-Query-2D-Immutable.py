class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n, self.m = len(matrix[0]), len(matrix)
        self._prefix = [[0] * (self.n + 1) for _ in range(self.m + 1)] 
        for r in range(len(self._prefix) - 1 ):
            for c in range(len(self._prefix[0])-1):
                self._prefix[r+1][c+1]=matrix[r][c] + self._prefix[r][c+1] + self._prefix[r+1][c] - self._prefix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._prefix[row2+1][col2+1] - self._prefix[row1][col2+1] - self._prefix[row2+1][col1] + self._prefix[row1][col1]
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
