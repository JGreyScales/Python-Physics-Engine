import math
class formulas:
    def __init__(self) -> None:
        pass

    def inverse(i):
        return i - (i * 2)

    ## calculates and returns terminal velocity 
    def calculate_terminal_velocity(self, m, g, c, p, a): #Mass, Gravity, Coefficent, Density of air, Projected area
        return math.sqrt((2*m*g)/(c*p*a))
a = formulas