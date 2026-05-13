class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for j in range(9):
                if board[row][j] == ".":
                    continue
                if board[row][j] in seen:
                    return False
                seen.add(board[row][j])
        
        for col in range(9):
            seen = set()
            for j in range(9):
                if board[j][col] == ".":
                    continue
                if board[j][col] in seen:
                    return False
                seen.add(board[j][col])

        for square in range(9):
            #Set for each 3x3 square
            seen = set()
            for i in range(3):
                for j in range(3):
                    # 3 Positions per row, so square <= 3. row 0, 4 - 6: row 3, (why we multiply)
                    row = square // 3 * 3 + i
                    #Column changes each iteration
                    col = square % 3 * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True
        
        