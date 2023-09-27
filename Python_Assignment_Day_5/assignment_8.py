class Circle:
    pass
    
def calculate_area(c):
        c.area = 3.14 * (c.radius ** 2)
        

def calculate_perimeter(c):
        c.perimeter = 2 * 3.14 * c.radius
        # return c.perimeter

def info(c):
        return f"Circle with radius : {c.radius}\nPerimeter : {c.perimeter}\nArea : {c.area} "

def draw(c):
    print(info(c))
    
        
def create_Circle(radius):
    c=Circle()
    if(radius>0):
        
        c.radius=radius
        calculate_area(c)
        calculate_perimeter(c)
        draw(c)
    else:
        print('Please enter a valid radius')
     
create_Circle(4)