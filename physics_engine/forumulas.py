1

#cd = (Cube, CD = 0.8, frontal area s2) - 0.8 (s2)


#Fd = cd 1/2 ρ v2 A                
## fd = 0.8 1/2 p v2 A
##we need to calculate drag coefficent

# Cd = D / (q * A)
# CD = dq




import math
def calculate_terminal_velocity(m, g, c, p, a): #Mass, Gravity, Coefficent, Density of air, Projected area
    print(g)
    print("Python Program to calculate Terminal Velocity:") 
    print("-------------------------------------------")

    print("Mass of the falling object:    ", m) 
    print("Acceleration due to gravity: ", g) 
    print("Drag coefficient:     ",c) 
    print("Density of the fluid through which the object is falling:     ",p) 
    print("Projected area of the object:     ",a) 

    #TerminalVelocity = Vt = sqrt ( (2 * m * g) / (Cd * ρ * A))
    terminal_velocity =  math.sqrt((2*m*g)/(c*p*a))

    print('-------------------------------------------')
    print("Terminal Velocity  Calculated:   ", terminal_velocity)

  
calculate_terminal_velocity(300, 9.81 / 3, 1.05, 1.225, 20)



#https://www.engineeringtoolbox.com/drag-coefficient-d_627.html"""