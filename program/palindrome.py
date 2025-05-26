a = int (input("Enter a value : "))

def palindrome(a):
    s = str(a) 
    s == s[::-1]

print(palindrome(121))
print(palindrome(122))

a = ["1,2,3,2,1"]
def palindrome(a):
    
    if a == a[::-1]:
        print("1229")
    else:
        print("123")

print(palindrome(a))


list1=[1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("yes")
else:
    print("no")
