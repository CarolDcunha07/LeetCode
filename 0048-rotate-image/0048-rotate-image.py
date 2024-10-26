class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols=len(matrix[0])
        rows=len(matrix)
        n=len(matrix)
        
        ans=[[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                ans[j][n-i-1]=matrix[i][j]
                
                
        for i in range(rows):
            for j in range(cols):
                matrix[i][j]=ans[i][j]
        return matrix
                         
        