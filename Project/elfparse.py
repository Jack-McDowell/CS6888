def get_function_bounds(project, function_name):
    """
    Returns (start address, end address) for the given function in
    the ANGR project passed as an argument.
    """
    pass

def get_var_stack_offset(project, function_name, var_name):
    """
    Returns the offset from the stack pointer's value at the beginning 
    of the function to the variable's location on the stack. In general,
    rsp + offset, where rsp holds the value of register rsp at the start
    of the function and offset is the return value of this function 
    should refer to the memory address of the variable. 
    """