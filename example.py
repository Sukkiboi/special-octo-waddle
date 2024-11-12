# SquareSidelength=eval(input("enter the side of the square"))
# SquarePerimeter=4*SquareSidelength
# print(SquarePerimeter)

# RadiusOfCircle=eval(input("enter the radius of the circle: "))
# from math import pi
# Circumference=2*pi*RadiusOfCircle
# print(Circumference)

MRP=eval(input("enter the MRP of the product: "))
SP=eval(input("enter the selling price of the product: "))
Discount=MRP-SP
Discount_Per=Discount/MRP*100
print(Discount_Per)