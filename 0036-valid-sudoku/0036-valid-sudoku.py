class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValidGroup(group):
            elements = [num for num in group if num != '.']
            return len(elements) == len(set(elements))

        for row in board:
            if not isValidGroup(row):
                return False

        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not isValidGroup(column):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                sub_box = [
                    board[r][c]
                    for r in range(box_row, box_row + 3)
                    for c in range(box_col, box_col + 3)
                ]
                if not isValidGroup(sub_box):
                    return False

        return True