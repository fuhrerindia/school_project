print("HUE HUE HUE CODE!")
print("1-x+x^1-x^2+....x^n")

# DEFINING FUNCTION TO CHECK IF THE IT'S EVEN OR ODD TERM
def isEven(num):
    if (num%2 == 0):
        return True
    else:
        return False

def factorial(num):
    output = 1
    for v in range(num):
        if (v != 0):
            output = output * v
    return output*num
#ASKING FOR input
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: ")) + 1
# DEFINING A DEFAULT VALUE
v = 0
#RUNNING SUM OF
for i in range(n):
    if (i != 0):
        if (isEven(i)):
            o = v
            v = v + ((x**i)/factorial(i))
        else:
            o = v
            if (i == 1):
                v = v + ((x**i)/factorial(i))
            else:
                v = v - ((x**i)/factorial(i))
print(f'OUTPUT: {v}')
print("HUEHUEHUE")