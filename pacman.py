class Pacman:
    """A Pac-Man character that tracks position and collected pellets."""

    def __init__(self, x=0, y=0):
        self._position = (x, y)
        self._pellets = 0

    def move(self, dx, dy=0):
        """Move by dx and dy (or move in a named direction)."""
        if isinstance(dx, str):
            directions = {
                "up": (0, 1),
                "down": (0, -1),
                "left": (-1, 0),
                "right": (1, 0),
            }
            if dx.lower() not in directions:
                raise ValueError("Direction must be up, down, left, or right")
            dx, dy = directions[dx.lower()] 

        x, y = self._position
        self._position = (x + dx, y + dy)

    def getPosition(self):
        """Return the current (x, y) position."""
        return self._position

    def collectPellet(self):
        """Collect one pellet and return the new total."""
        self._pellets += 1
        return self._pellets
