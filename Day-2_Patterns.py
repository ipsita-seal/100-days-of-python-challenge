#1. right triangle pattern
print("1. right triangle pattern")
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()
print("\n")

#2. Inverted Triangle Pattern
print("2. Inverted Triangle pattern")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print("\n")

#3. Pyramid Pattern
print("3. Pyramid pattern")
for i in range(5):
    for j in range(5 - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

#4. Number Triangle Pattern
print("4. Number Triangle pattern")
for i in range(5):
    for j in range (1, i+2):
        print(j, end="")
    print()
