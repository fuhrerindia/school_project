print("CHEEMS AND DOGGE ENGLISH!")
word = input("Enter something in cheems language! ")
word = word.lower()
vowel_count = {}
for vowel in "aeiou":
    count = word.count(vowel)
    vowel_count[vowel] = count
count = vowel_count.values()
total_vowels = sum(count)
consonents = len(word) - total_vowels

l,u = 0,0
for i in word:
    if (i>='a'and i<='z'):
        l=l+1                 
    if (i>='A'and i<='Z'):
        u=u+1   

print(f'VOWELS: {total_vowels}')
print(f'CONSONENTS: {consonents}')
print('Lower case characters: ',l)
print('Upper case characters: ', len(word) - l)