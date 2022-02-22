class Vetor: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

def __repr__(self):
    return f"Vetor({self.x},{self.y})"
