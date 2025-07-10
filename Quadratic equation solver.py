import math

# Read coefficients a, b, and c from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Check if it's a valid quadratic equation (a ≠ 0)
if a == 0:
    print("This is not a quadratic equation.")
else:
    # Compute the discriminant (delta)
    delta = b**2 - 4*a*c

    if delta < 0:
        # No real roots
        print("No real roots.")
    elif delta == 0:
        # One real root
        x = -b / (2*a)
        print(f"One real root: x = {x}")
    else:
        # Two real roots
        sqrt_delta = math.sqrt(delta)
        x1 = (-b - sqrt_delta) / (2*a)
        x2 = (-b + sqrt_delta) / (2*a)
        print(f"Two real roots: x1 = {x1}, x2 = {x2}")
