import string

def alphabets(c1, c2):
    alphabet = string.ascii_lowercase  # string.ascii_lowercase is 'a to z'->find the index of c1 and c2 in this string.
    start = alphabet.index(c1)
    end = alphabet.index(c2)
    for ch in alphabet[start:end+1]:
        print(ch, end=' ')
alphabets('a', 'z')


number = 12
print("Binary equivalent:", bin(number)[2:])

"""Other method without using string module"""
# def alphabets(c1, c2):
#     for ch in range(ord(c1), ord(c2) + 1): #range from ASCII value of c1 to ASCII value of c2
# #The ord() function returns the ASCII (or Unicode) value of a character. Ex: ord('a') → 97, ord('z') → 122
#                     #If c1 = 'a' and c2 = 'd', this  for ch in range(97, 100+1):  # 97, 98, 99, 100

#         print(chr(ch), end=' ')

# alphabets('a', 'z')
