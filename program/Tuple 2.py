def sequence(tup):
    diff = tup[1] - tup[0]
    last = tup[-1]
    
    new_ter= [last + diff * i for i in range(1, 4)]
    
    return tup + tuple(new_ter)
tup=(1,7,23,7)
print(sequence(tup))