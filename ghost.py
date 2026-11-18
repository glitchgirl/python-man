import random


class Ghost:
    """A simple ghost that can move around and chase Pac-Man."""

    DIRECTIONS = ("up", "down", "left", "right")

    def __init__(self, x=0, y=0, direction="left"):
        self.x = x
        self.y = y
        self.changeDirection(direction)

    def changeDirection(self, direction):
        """Set the ghost's direction to one of the four valid directions."""
        if direction not in self.DIRECTIONS:
            raise ValueError("direction must be up, down, left, or right")
        self.direction = direction

    def move(self):
        """Move one position in the current direction."""
        if self.direction == "up":
            self.y -= 1
        elif self.direction == "down":
            self.y += 1
        elif self.direction == "left":
            self.x -= 1
        elif self.direction == "right":
            self.x += 1

    def chasePacman(self, pacman_x, pacman_y):
        """Choose a direction that reduces the distance to Pac-Man."""
        dx = pacman_x - self.x
        dy = pacman_y - self.y

        if abs(dx) >= abs(dy) and dx != 0:
            self.changeDirection("right" if dx > 0 else "left")
        elif dy != 0:
            self.changeDirection("down" if dy > 0 else "up")

        self.move()
