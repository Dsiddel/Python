""" this program takes a circle or triangle and generates are of the object as output"""

print("Calculator is starting up")

option = input("Enter C for Circle or T for Triangle ")
option = option.lower()

if option == "c":
  radius = float(input("What's the radius"))
  area = 3.14159 * radius ** 2
  print(str(area))
elif option == "t":
  base = float(input("what's the base of the triangle? "))
  height = float(input("what's the height of the triangle? "))
  area = .5 * base * height
  print(str(area))
else:
  print("you picked wrong")
  
print("the program is exiting")