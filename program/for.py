str = "hello_world"



str.index('he')
str.index('o')
str.index('o',5)
# str.index('o',8)


str1 = 'hello_python'
str1.rindex('o',0,5)
str1.rindex('o',-11,5)
str1.rindex('')
print(str1)

str2 = 'python hello'
str2.rfind('o')
str.rfind('1',2,9)
str2.rfind('1',2,10)
str2.rfind('on',2,8)


# string methods
# boolen methods
# isupper(): it retuen true if and the string is uppercase else flase



s = 'APPLE'
s.isupper () #True

s1 = "Python"
s1.isupper() #False

#isalnum() it the retuen true the string contains only alphabets, only digits,

s2 = "python 1991"
s2.isalnum() #False

s3 = "99this is true"
s3.isalnum() #true

#isdigit() only digit is true
s4="kjd12"
s4.isdigit()

s5="234524"
s5.isdigit()

#indexing : the process of extarcting single element form list 

name =['apple', 'google', 'yahoo', 'gmail',['java', 'c', 'python', 'ruby'], 'wal']

print(name[4][1])

