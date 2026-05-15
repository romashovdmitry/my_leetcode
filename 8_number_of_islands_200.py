from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        islands = 0
        rows, cols = len(grid), len(grid[0])

        def helper(helper_row, helper_col):

            if (
                helper_row < 0
                or helper_row >= rows
                or helper_col < 0
                or helper_col >= cols
                or grid[helper_row][helper_col] != "1"
            ):

                return

            grid[helper_row][helper_col] = "2"

            helper(helper_row + 1, helper_col)
            helper(helper_row - 1, helper_col)
            helper(helper_row, helper_col + 1)
            helper(helper_row, helper_col - 1)

        for row in range(rows):

            for col in range(cols):

                if grid[row][col] == "1":
                    helper(row, col)
                    islands += 1

        return islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(Solution().numIslands(grid))