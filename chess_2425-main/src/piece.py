from src.color import Color


class Piece:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color



    def __str__(self):
        c = 'w' if self.color == Color.WHITE else 'b'
        return f'{c}{self.char()}'



