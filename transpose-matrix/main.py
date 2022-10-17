class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = []
        for c in range(len(matrix[0])):
            new_row = []
            for r in range(len(matrix)):
                new_row.append(matrix[r][c])
            new_matrix.append(new_row)
            
        return new_matrix