try:
    import numpy
except ModuleNotFoundError:
    print("is not installed.")
else:
    print("is installed.")

# try:
#    module_name = input("Enter a module name: ")
   
#    if module_name != "math":
#       raise ModuleNotFoundError(f"\nNo found module{module_name}")
    
#    else:
#        import math
#        print("This is insatll module")
# except ModuleNotFoundError as module:
#     print(f"not a used {module}")