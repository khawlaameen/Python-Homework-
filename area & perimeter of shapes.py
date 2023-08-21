class calculator:
    def __init__(self):
        print("welcome")
        
    def calculate_area_of_triangle(self,base,height):
        self.base=base
        self.height=height
        print((base*height)/2);
    
    def calculate_perimeter_of_triangle(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print(a+b+c);
        
    def calculate_area_of_circle(self,half_radius,pi=3.14):
        self.half_radius=half_radius
        print(pi*half_radius*half_radius);

        
    def calculate_perimeter_of_circle(self,half_radius,pi=3.14):
        self.half_radius=half_radius
        print(2*pi*half_radius);

        
    def calculate_area_of_rectangle(self,base,height):
        self.base=base
        self.height=height
        print(base*height);

        
    def calculate_perimeter_of_rectangle(self,base,height):
        self.base=base
        self.height=height
        print(2*(base+height));

    
    def calculate_area_of_square(self,rib_of_square):
        self.rib_of_square=rib_of_square
        print(rib_of_square*rib_of_square);

        
    def calculate_perimeter_of_square(self,rib_of_square):
        self.rib_of_square=rib_of_square
        print(rib_of_square*4);

        
        
obj=calculator()
print(" 1)area of triangle\n 2)primeter of triangle\n 3)area of circle\n 4)primeter of circle \n 5)area of rectangle\n 6)primeter of rectangle\n 7)area of square\n 8)primeter of square")
choice=input("chose a number:")


if  choice == "1":
    base=float(input("input the base of triangle"))
    height=float(input("input the height of triangle"))
    obj.calculate_area_of_triangle(base,height)
    
elif choice =="2":
    rib1=float(input("input rib1 of triangle"))
    rib2=float(input("input rib2 of triangle"))
    rib3=float(input("input rib3 of triangle"))
    obj.calculate_perimeter_of_triangle(rib1,rib2,rib3)
    
elif  choice == "3":
    half_radius=float(input("input the half radius of the circle"))
    obj.calculate_area_of_circle(half_radius)
    
elif  choice == "4":
    half_radius=float(input("input the half radius of the circle"))
    obj.calculate_perimeter_of_circle(half_radius)
    
elif  choice == "5":
    base=float(input("input the base of rectangle"))
    height=float(input("input the height of rectangle"))
    obj.calculate_area_of_rectangle(base,height)
    
elif  choice == "6":
    base=float(input("input the base of rectangle"))
    height=float(input("input the height of rectangle"))
    obj.calculate_perimeter_of_rectangle(base,height)
    
elif choice== "7":
    rib_of_square=float(input("input the rib of square"))
    obj.calculate_area_of_square(rib_of_square)
    
elif choice== "8":
    rib_of_square=float(input("input the rib of square"))
    obj.calculate_perimeter_of_square(rib_of_square)
    
else:
    print("wrong input!")
        