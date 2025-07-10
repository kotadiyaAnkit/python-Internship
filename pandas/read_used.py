import pandas as pa

data = {
    'car' : ["m1","m2","m3"],
    'passing': [2001, 2002, 2003],
     
    
}

print("version",pa.__version__)
mydata = pa.DataFrame(data)

print(mydata)
