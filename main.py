def number_triangle(rows):
    print("\nNumber Triangle:\n")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
def reverse_triangle(rows):
    print("\nReverse Number Triangle:\n")
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
def number_pyramid(rows):
    print("\nNumber Pyramid:\n")
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()
while True:
    print("\n" + "=" * 35)
    print("   NUMBER PATTERN GENERATOR")
    print("=" * 35)
    print("1. Number Triangle")
    print("2. Reverse Number Triangle")
    print("3. Number Pyramid")
    print("4. Exit")
    choice = input("Enter Choice: ")
    if choice == "4":
        print("Thank You!")
        break
    try:
        rows = int(input("Enter Number of Rows: "))
        if rows <= 0:
            print("Please enter a positive number.")
            continue
        if choice == "1":
            number_triangle(rows)
        elif choice == "2":
            reverse_triangle(rows)
        elif choice == "3":
            number_pyramid(rows)
        else:
            print("Invalid Choice!")
    except ValueError:
        print("Please enter a valid number.")