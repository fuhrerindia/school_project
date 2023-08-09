string = input("ENTER SOMETHING....: ")
def isPalindrome(s):
    s = str(s)
    if (s == s[::-1]):
        print(f'{s} is a palendrome!')
    else:
        print(f'{s} is not a palendrome!')
print(f'SWITCHED CASE: \n{string.swapcase()}')
isPalindrome(string)