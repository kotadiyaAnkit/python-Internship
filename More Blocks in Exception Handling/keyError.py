thisdict = {
  "jack": "xyz",
  "stream": "bca",
  "year": 1964
}

try:
    print(thisdict["stream"])  
except KeyError:
    print("That is not a valid key.")
else:
    print("That is a valid key.")
