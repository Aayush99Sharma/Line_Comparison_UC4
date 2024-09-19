import math

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_length(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

if __name__ == "__main__":
    line = Line(0, 0, 3, 4)
    print(f"Length of the line: {line.calculate_length()}")
