from offsets import get_var_offset
cfgs = {}
func_bounds = {}
var_offset = {}

def get_function_bounds(project, function_name):
    """
    Returns (start address, end address) for the given function in
    the ANGR project passed as an argument.
    """
    id_tup = (project, function_name)
    global cfgs
    global func_bounds
    if project not in cfgs:
        cfgs[project] = project.analyses.CFGFast()
    cfg = cfgs[project]
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
    id_tup = (project, function_name, var_name)
    global var_offset
    if id_tup in var_offset:
        return var_offset[id_tup]
    print(project.filename)
    var_offset[id_tup] = get_var_offset(project.filename, function_name.encode('utf-8'), var_name.encode('utf-8'))
    return var_offset[id_tup]