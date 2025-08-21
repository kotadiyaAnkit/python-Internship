a = 4
for i in range(a):
    for j in range(a):
        print('*', end=' ')
    print()
    
print("---------------------------------------------")
    
n = 4
for i in range(n):  #i is the row number (from 0 to n-1).
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            #i == 0: First row i == n - 1: Last row j == 0: First column j == n - 1: Last column
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#(0,0) (0,1) (0,2) (0,3)
#(1,0) (1,1) (1,2) (1,3)
#(2,0) (2,1) (2,2) (2,3)
#3,0) (3,1) (3,2) (3,3)
