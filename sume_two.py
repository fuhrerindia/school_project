print("HUE HUE HUE CODE!")
print("1-x+x^1-x^2+....x^n")

# DEFINING FUNCTION TO CHECK IF THE IT'S EVEN OR ODD TERM
def isEven(num):
    if (num%2 == 0):
        return True
    else:
        return False

#ASKING FOR input
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: ")) + 1
#DEFINING A DEFAULT VALUE
v = 0
#RUNNING SUM OF
for i in range(n):
    if isEven(i):
        v = v + (x**i)
    else:
        v = v - (x**i)
print(v)
print("HUEHUEHUE")