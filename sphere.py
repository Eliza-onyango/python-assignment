import math

# Get user input for the radius
Radius = float(input("Enter the radius of the sphere: "))
# Calculate the volume of the sphere
volume = (4/3) * math.pi * Radius**3

print(f"The volume of the sphere  is: {volume:.2f}")