def Fahrenheit (degree):
    #the equations needed to calculate celsius 
        number = degree-32
        Celsius = number*5/9
        print Celsius
        
def height (x1,x2,h): 
    #the equation to find trapezoid area 
    A = (x1 + x2)*h
    #used divided by 2.00 to find the answer to the decimal
    Area = A/2.00
    print Area 
    
def radius (number):
    #imported math.function to make it easier also for more exact answer
    import math
    Area = 0
    Area = math.pi * 2**number 
    print Area
    
