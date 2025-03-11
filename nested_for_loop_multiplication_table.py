for i in range(1, 6):
    for j in range(1, 6):  # Inner loop indented
        product = i * j  # Calculate product
        print(f"{product:4}", end="")  # Print product with 4 spaces
    print()  # New line after inner loop
