try:
    # Get the number and root degree from the user
    number = float(input("Enter the number: "))
    n = float(input("Enter the root degree: "))

    # Root degree cannot be zero
    if n == 0:
        raise ValueError("Root degree cannot be zero.")

    # Compute the n-th root
    result = number ** (1 / n)
    print(f"The {n}-th root of {number} is: {result}")
except ValueError as e:
    # Handle invalid input or zero root degree
    print("Error:", e)
except Exception:
    # Handle other errors (e.g. complex result)
    print("Operation cannot be performed.")
