def PerfectNumber(Number):
    Sum = 0
    for i in range(1, Number):
        if(Number % i == 0):
            Sum = Sum + i
    if (Sum == Number):
        print(" %d is a Perfect Number" %Number)
    else:
        print(" %d is not a Perfect Number" %Number)

def Armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    # display the result
    if num == sum:
        print(f'{num} is an Armstrong number')
    else:
        print(f'{num} is not an Armstrong number')
def isPalindrome(s):
    s = str(s)
    if (s == s[::-1]):
        print(f'{s} is a palendrome!')
    else:
        print(f'{s} is not a palendrome!')
print("HUEHUEHUE")
print("FIND IF A NUMBER IS PERFECT, IS PELINDROME AND IS ARMSTRONG NUM OR NOT....")
val = int(input("ENTER A CHEEMS NUMBER: "))
PerfectNumber(val)
Armstrong(val)
isPalindrome(val)