from offsets import get_var_offset, get_func_bounds, get_frame_base
func_bounds = {}
var_offset = {}

def get_function_bounds(project, function_name):
    """
    Returns (start address, end address) for the given function in
    the ANGR project passed as an argument.
    """
    id_tup = (project, function_name)
    global func_bounds
    if id_tup in func_bounds:
        return func_bounds[id_tup]
    bound_offsets = get_func_bounds(project.filename, function_name.encode('utf-8'))
    func_bounds[id_tup] = (bound_offsets[0] + project.loader.memory.min_addr,
                           bound_offsets[1] + project.loader.memory.min_addr)
    return func_bounds[id_tup]


def get_var_stack_offset(project, function_name, var_name, base):
    """
    Returns the offset from the stack pointer's value at the beginning 
    of the function to the variable's location on the stack. In general,
    rsp + offset, where rsp holds the value of register rsp at the start
    of the function and offset is the return value of this function 
    should refer to the memory address of the variable. 
    """
    id_tup = (project, function_name, var_name)
    global var_offset
    if id_tup in var_offset:
        return var_offset[id_tup]
    var_offset[id_tup] = get_var_offset(project.filename, function_name.encode('utf-8'), var_name.encode('utf-8'))
    # COMMENT OUT THE BELOW LINE TO GET WRONG OFFSET
    # GETS RIGHT OFFSET FOR locals.c AT LEAST
    var_offset[id_tup] += get_frame_base(project.filename, base, project.loader.memory.min_addr)
    print("Offset for " + var_name + " is " + hex(var_offset[id_tup]))
    return var_offset[id_tup]
