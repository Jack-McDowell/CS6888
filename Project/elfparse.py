cfg = {}
func_bounds = {}


def get_function_bounds(project, function_name):
    """
    Returns (start address, end address) for the given function in
    the ANGR project passed as an argument.
    """
    id_tup = (project, function_name)
    global cfg
    global func_bounds
    if project not in cfg:
        cfg = project.analyses.CFGFast()
    if id_tup in func_bounds:
        return func_bounds[id_tup]
    func = cfg.kb.functions.function(name=function_name)
    end_addr = 0
    for block in func.blocks:
        if block.instruction_addrs[block.instructions - 1] > end_addr:
            end_addr = block.instruction_addrs[block.instructions - 1]
    func_bounds[id_tup] = (func.addr, end_addr)
    return func_bounds[id_tup]


def get_var_stack_offset(project, function_name, var_name):
    """
    Returns the offset from the stack pointer's value at the beginning 
    of the function to the variable's location on the stack. In general,
    rsp + offset, where rsp holds the value of register rsp at the start
    of the function and offset is the return value of this function 
    should refer to the memory address of the variable. 
    """