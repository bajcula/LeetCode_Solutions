class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        sum = 0
        
        for i in range(n):
            sum += mat[i][i]
            sum += mat[i][n-1-i]
            
        if not n % 2 == 0:
            middle = round((n - 1) / 2)
            sum -= mat[middle][middle]
            
        return sum