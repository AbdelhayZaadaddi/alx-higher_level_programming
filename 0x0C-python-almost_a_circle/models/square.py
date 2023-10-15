from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter method for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size."""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
