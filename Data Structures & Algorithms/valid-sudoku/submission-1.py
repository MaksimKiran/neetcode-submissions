def hasDuplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            newRow = [el for el in row if el != "."]
            if hasDuplicate(newRow):
                return False
        cols = [[row[i] for row in board]for i in range(len(board[0]))]
        for col in cols:
            newCol = [el for el in col if el != "."]
            if hasDuplicate(newCol):
                return False
        squares = [
            [board[r+i][c+j] for i in range(3) for j in range(3)]
            for r in range(0,len(board),3)
            for c in range(0,len(board),3)
        ]

        for square in squares:
            newSquare = [el for el in square if el != "."]
            if hasDuplicate(newSquare):
                return False

        return True
