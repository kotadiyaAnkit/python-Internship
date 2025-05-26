
# Step 1: Create a user-defined exception class
class MarksTooHighError(Exception):
    """Custom exception for marks greater than 100"""
    def __init__(self, mark, message):
        self.mark = mark
        self.message = message
        super().__init__(self.message)
        

class marks():
    def check_marks(mark):
     if mark > 100:
        raise MarksTooHighError(mark, "Marks are too high!")
     else:
        print(f"Marks entered: {mark}")
    

    try:
        check_marks(12)  # Valid 
        check_marks(120)  # - raises 
    except MarksTooHighError as e:
        print(f"Custom Exception: {e}")
