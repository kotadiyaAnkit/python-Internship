class TemporaryListModification:
    def __init__(self, target_list):
        self.target_list = target_list
        self._original = None

    def __enter__(self):
        # Makeing copy of the list to preserve the original list
        self._original = self.target_list[:] #  copy the list.
        return self.target_list #Returns the list so you can modify it inside the with block.

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:  #(exc_type is not None), we restore the original list.
            
            # An exception occurred, restore the original list
            self.target_list[:] = self._original
        # Returning False allows exception to propagate (if needed)
        
        return False  #False valuse call raised.
    
    #brform with
my_list = [1, 2, 3]

try:
    with TemporaryListModification(my_list) as lst: #
        lst.append(4) # to the list
        lst.remove(1)
        raise ValueError() #Target exit
        
    # Simulating an error
except ValueError:
    pass

print(my_list)  # Output: [1, 2, 3] — original list restored due to exception

# Successful modification example
with TemporaryListModification(my_list) as lst:
    lst.append(5)

print(my_list)  # Output: [1, 2, 3, 5] — changes persisted
