import random

class Maze:
    """Represent and render a text-based maze level."""

    def __init__(self, level=None):
        self.grid = []
        if level is None:
            self.generateLevel()
        else:
            self.loadLevel(level)

    def generateLevel(self, width=15, height=11, seed=None):
        """Generate a connected maze with wall and floor tiles."""
        if width < 5 or height < 5 or width % 2 == 0 or height % 2 == 0:
            raise ValueError("width and height must be odd numbers of at least 5")

        rng = random.Random(seed)
        self.grid = [["#"] * width for _ in range(height)]
        stack = [(1, 1)]
        self.grid[1][1] = " "

        # Walk through the maze like a depth-first search, backtracking when
        # the current corridor has no unvisited cells left to explore.
        while stack:
            x, y = stack[-1]
            # A candidate is two cells away so the cell between them can become
            # the connecting corridor. Keep candidates inside the outer wall
            # and only visit cells that are still walls.
            neighbors = [
                (x + dx, y + dy, dx, dy)
                for dx, dy in ((0, -2), (2, 0), (0, 2), (-2, 0))
                if 0 < x + dx < width - 1
                and 0 < y + dy < height - 1
                and self.grid[y + dy][x + dx] == "#"
            ]

            if not neighbors:
                # This path is finished; return to the previous junction.
                stack.pop()
                continue

            # Pick a random unvisited cell, open the wall between it and the
            # current cell, then continue exploring from the new cell.
            next_x, next_y, dx, dy = rng.choice(neighbors)
            self.grid[y + dy // 2][x + dx // 2] = " "
            self.grid[next_y][next_x] = " "
            stack.append((next_x, next_y))

    def loadLevel(self, level):
        """Load a level from a multiline string, rows, or a file path."""
        if isinstance(level, str):
            if "\n" not in level:
                try:
                    with open(level, "r", encoding="utf-8") as level_file:
                        level = level_file.read()
                except OSError:
                    pass
            self.grid = [list(line) for line in level.splitlines()]
        else:
            self.grid = [list(row) for row in level]

        if not self.grid:
            return

        width = max(len(row) for row in self.grid)
        for row in self.grid:
            row.extend(" " * (width - len(row)))

    def drawMaze(self):
        """Print the current maze to the terminal."""
        for row in self.grid:
            print("".join(row))
