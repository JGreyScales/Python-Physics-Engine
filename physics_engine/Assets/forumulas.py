import math
class formulas:
    def __init__(self) -> None:
        pass

    # inverses a number 
    def inverse(i):
        return i - (i * 2)

    def to_positive(self, i):
        if i > 0:
            return i
        return i - (i * 2)
        
    ## calculates and returns terminal velocity 
    def calculate_terminal_velocity(self, m, g, c, p, a): #Mass, Gravity, Coefficent, Density of air, Projected area
        return math.sqrt((2*m*g)/(c*p*a))

        
    def vector_angle(I_dont_want_to_fix_this, current_pos, *args):
      old_pos = args[0]
      if old_pos == current_pos: return 0
      print(current_pos, old_pos)
      try:
        slope = (current_pos[1] - current_pos[0]) / (old_pos[1] - old_pos[0])
        theta = abs(math.atan(slope) - 1) * 100
        print(theta)
      except(ZeroDivisionError): return 0