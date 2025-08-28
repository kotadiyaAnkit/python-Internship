#User function Template for python3
n = int(input())

if n<=1:   #We check n <= 1: Not prime → print "False"
    print("False")
else:     
    for i in range(2 , int(n **0.5) +1):
        if n % i ==0:    #If n % i == 0: Not prime → print "False" and stop
            print("False")
            break
    else:
        print("True")
    

