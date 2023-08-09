print("HUE HUE HUE CODE!")
print("1+x+x^1+x^2+....x^n")
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: ")) + 1
v = 0
for i in range(n):
    v = v + (x**i)
print(v)