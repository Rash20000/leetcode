# https://leetcode.com/problems/valid-sudoku/submissions/1097901306/
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
        table_buffer = dict()

        def calculate_quadrant(row, col) -> int:
            if (0 <= row <= 2) and (0 <= col <= 2):
                return 1
            elif (0 <= row <= 2) and (3 <= col <= 5):
                return 2
            elif (0 <= row <= 2) and (6 <= col <= 8):
                return 3

            elif (3 <= row <= 5) and (0 <= col <= 2):
                return 4
            elif (3 <= row <= 5) and (3 <= col <= 5):
                return 5
            elif (3 <= row <= 5) and (6 <= col <= 8):
                return 6

            elif (6 <= row <= 8) and (0 <= col <= 2):
                return 7
            elif (6 <= row <= 8) and (3 <= col <= 5):
                return 8
            elif (6 <= row <= 8) and (6 <= col <= 8):
                return 9
            else:
                raise ValueError("Invalid grid coordinates!")

        def update_table_buffer(item: str, row: int, col: int) -> None:
            table_buffer[item]['ROW'].update({row: True})
            table_buffer[item]['COL'].update({col: True})
            table_buffer[item]['QUAD'].update({calculate_quadrant(row, col): True})

        for row, row_item in enumerate(board):
            for pos, item in enumerate(row_item):
                if item == self.BLANK:
                    continue
                elif item not in table_buffer:
                    logging.debug(f"Newly discovered digit -> {item}")
                    table_buffer.update({item: {
                        'ROW': {},
                        'COL': {},
                        'QUAD': {},
                    }})
                    update_table_buffer(item, row, pos)
                else:
                    logging.debug(f"Check if item is in same 3x3 matrix")
                    logging.debug(f"Check if item is in same row col")

                    if table_buffer[item]['QUAD'] == calculate_quadrant(row, pos):
                        return False

                    elif table_buffer[item]['ROW'] == row:
                        return False
                    elif table_buffer[item]['COL'] == pos:
                        return False
                    else:
                        update_table_buffer(item, row, pos)

        return True


# Example usage:
dummy_input = [
    [".", ".", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "8", ".", ".", ".", "3", "."],
    [".", "5", ".", ".", "2", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "9"],
    [".", ".", ".", ".", ".", ".", "4", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "7"],
    [".", "1", ".", ".", ".", ".", ".", ".", "."],
    ["2", "4", ".", ".", ".", ".", "9", ".", "."]
]

print(Solution().isValidSudoku(dummy_input))
