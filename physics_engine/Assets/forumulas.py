import math
class formulas:
    def __init__(self) -> None:
        pass

    # returns an inverse of i
    def inverse(self, i):
        return i - (i * 2)

    def to_positive(self, i):
        if i > 0:
            return i
        return i - (i * 2)

    ## calculates and returns terminal velocity 
    def calculate_terminal_velocity(self, m, g, c, p, a): #Mass, Gravity, Coefficent, Density of air, Projected area
        return math.sqrt((2*m*g)/(c*p*a))
