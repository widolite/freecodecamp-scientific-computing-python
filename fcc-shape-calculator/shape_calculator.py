class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):

        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width**2 + self.height**2)**.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture_width = "*" * self.width
        picture_heigth = ""
        for y in range(self.height):
            picture_heigth += "{}\n".format(picture_width)

        return picture_heigth.format(picture_width)

    def get_amount_inside(self, shape):

        wide_shape = self.width // shape.width
        height_shape = self.height // shape.height

        return wide_shape * height_shape


class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return "Square(side={})".format(self.side)

    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)
        self.side = side

