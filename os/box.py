def area(l,w):
    return print(f" Area = { l * w}")

def perimeter(l,w):
    return print(f"Perimeter = { l + w + l + w}")

def volume(l,w,h):
    return print(f"volume = {l* w * h}")

def surfaceArea(l,w,h):
    return print(f"SurfaceArea = {(l*w*2)+(l*h*2)+(w*h*2)}")

print("Enter ur number to calculate Area*Perimeter*Volume*SurfaceArea")
l = int (input("Enter ur number to calculate Lenght: "))
w = int (input("\nEnter ur number to calculate width: "))
h = int (input("\nEnter ur number to calculate Height: "))

area(l,w)
perimeter(l,w)
volume(l,w,h)
surfaceArea(l,w,h)
