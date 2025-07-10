import time
from contextlib import contextmanager  

@contextmanager
def timer():
    start_time = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start_time
        print(f"[Function Timer] Elapsed time: {elapsed:.4f} seconds")

# Example usage
with timer():
    print("Running another task...")
    time.sleep(1.5)

