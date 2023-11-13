# https://leetcode.com/problems/valid-sudoku/submissions/1097913064
# row can have digits betwen 1-9 and . (empty)
# digit should not be in same row, col or 3x3 grids of the og table 
# _|_|_||_|_|_||_|_|_
# _|_|_||_|_|_||_|_|_
# =|=|=||=|=|=||=|=|=
# _|_|_||_|_|_||_|_|_
# _|_|_||_|_|_||_|_|_
# =|=|=||=|=|=||=|=|=
# _|_|_||_|_|_||_|_|_
# _|_|_||_|_|_||_|_|_
# =|=|=||=|=|=||=|=|=
import logging


class Solution:
    BLANK = '.'

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        table_buffer:dict[str, dict[str, set]] = dict()

        def calculate_quadrant(row, col) -> int:
            return (row // 3) * 3 + col // 3 + 1

        def update_table_buffer(item: str, row: int, col: int) -> None:
            table_buffer[item]['ROW'].add(row)
            table_buffer[item]['COL'].add(col)
            table_buffer[item]['QUAD'].add(calculate_quadrant(row, col))


        for row, row_item in enumerate(board):
            for pos, item in enumerate(row_item):
                if item == self.BLANK:
                    continue
                elif item not in table_buffer:
                    logging.debug(f"Newly discovered digit -> {item}")
                    table_buffer.update({item: {
                        'ROW': set(),
                        'COL': set(),
                        'QUAD': set(),
                    }})
                    update_table_buffer(item, row, pos)
                else:
                    logging.debug(f"Check if item is in same 3x3 matrix")
                    logging.debug(f"Check if item is in same row col")

                    if calculate_quadrant(row, pos) in table_buffer[item]['QUAD']:
                        return False

                    elif row in table_buffer[item]['ROW']:
                        return False
                    elif pos in table_buffer[item]['COL']:
                        return False
                    else:
                        update_table_buffer(item, row, pos)

        return True


# Example usage:
dummy_input = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(dummy_input))
