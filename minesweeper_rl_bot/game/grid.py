import random
from string import ascii_lowercase


class Grid:
    def __init__(self, grid_size, num_bombs):
        self.grid_size = grid_size
        self.num_bombs = num_bombs
        self._create_grid()

    def _create_grid(self):
        """Create Minesweeper grid"""
        self.grid = [
            ["0" for i in range(self.grid_size)] for i in range(self.grid_size)
        ]

        self._set_mines()
        self._set_numbers()

    def _set_mines(self):
        """Add mines to empty grid"""
        mines = []
        for i in range(self.num_bombs):
            cell = self._get_random_cell()
            while cell in mines:
                cell = self._get_random_cell()
            mines.append(cell)
        for i, j in mines:
            self.grid[i][j] = "X"

    def _set_numbers(self):
        """Add numbers to grid with mines"""
        for rowno, row in enumerate(self.grid):
            for colno, cell in enumerate(row):
                if cell != "X":
                    # Gets the values of the neighbors
                    values = [
                        self.grid[r][c] for r, c in self._get_neighbors(rowno, colno)
                    ]

                    # Counts how many are mines
                    self.grid[rowno][colno] = str(values.count("X"))

    def _get_neighbors(self, rowno, colno):
        """Returns neighbors from a cell"""
        neighbors = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                elif (
                    -1 < (rowno + i) < self.grid_size
                    and -1 < (colno + j) < self.grid_size
                ):
                    neighbors.append((rowno + i, colno + j))

        return neighbors

    def _get_random_cell(self):
        """Returns random cell from grid"""
        a = random.randint(0, self.grid_size - 1)
        b = random.randint(0, self.grid_size - 1)

        return (a, b)

    def showgrid(self):
        """Returns formated grid string"""
        horizontal = "   " + (4 * self.grid_size * "-") + "-"

        # Print top column letters
        toplabel = "     "

        for i in ascii_lowercase[: self.grid_size]:
            toplabel = toplabel + i + "   "

        print(toplabel + "\n" + horizontal)

        # Print left row numbers
        for idx, i in enumerate(self.grid):
            row = "{0:2} |".format(idx + 1)

            for j in i:
                row = row + " " + j + " |"

            print(row + "\n" + horizontal)

        print("")
