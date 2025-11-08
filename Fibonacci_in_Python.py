def fibonacci(a):
    if a <= 0:
        return "Invalid input"
    elif a == 1 or a == 2:
        return 1
    else:
        b = fibonacci(a - 1) + fibonacci(a - 2)
        return b

x = int(input("Enter a positive integer: "))
print(f"The fibonacci sequence up to {x} is {fibonacci(x)}")
