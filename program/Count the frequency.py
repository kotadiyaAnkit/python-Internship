word = "hello worlld"
frequency = {}

for char in word:
    if char in frequency:#This checks whether the current character (char) is already a key in the frequency dictionary.
        frequency[char] += 1 #If the character is already in the dictionary, we increment its count by 1.
    else:
        frequency[char] = 1 

print(frequency)
