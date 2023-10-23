'''
NAME:KELVIN NZIOKA
REG_NO: PA106/G/9983/20
'''



global_variable = "I'm global" # Global variable

def variable_types():
    # Local variable
    local_variable = "I'm local"
    print(f"Inside the function: global_variable = {global_variable}")
    print(f"Inside the function: local_variable = {local_variable}")

# Accessing global variable outside the function
print(f"Outside the function: global_variable = {global_variable}")

# Trying to access the local variable outside the function (will result in an error)
# print(f"Outside the function: local_variable = {local_variable}")

variable_types()
