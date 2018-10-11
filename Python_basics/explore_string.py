str = input('Enter the string that you want to reverse: ')
print('Reversed string is :', str[::-1])
count = 0
for letter in str:
    if letter in 'aeiou':
        count += 1
print('Total number of characters in string is:', len(str))
print('Number of vowels are ', count)


# check for Palindrome
if str.lower().replace(" ", "") == str[::-1].lower().replace(" ", ""):
    print('This is a palindrom')

# Piglatin
words = []
no_of_words = 0
for word in str.lower().split(" "):
    no_of_words += 1
    if word[0] not in 'aeiou':
        words.append(word[1:]+'-'+word[0]+'ay')
    else:
        words.append(word+'-'+'ay')
words = " ".join(words)
print('The PigLatin version is ', words)
print('Total number of words in the string is ', no_of_words)

