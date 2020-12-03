from Operator import Operator, ExprType

class ASTNode:
    def __init__(self, operator, operands):
        assert(len(operands) == operator.operands)

        self.operator = operator
        self.operands = operands
        self.type = None
        self.string_representation = None
        self.memoization = None
        self.can_memoize = True
    
    def get_sym(self, state, lval=False):
        if self.memoization == None:
            val, not_state_invariant = self.operator.angrify(self.operands, state, lval)
            if self.can_memoize and not_state_invariant:
                for op in operands:
                    self.can_memoize = self.can_memoize and op.can_memoize
                if self.can_memoize:
                    self.memoization = val
            return val
        else:
            return self.memoization

    def stringify(self):
        if self.string_representation == None:
            children = [child.stringify() if type(child) is ASTNode else str(child) for child in self.operands]
            self.string_representation = self.operator.output(children)
        
        return self.string_representation

    def get_type(self, lval=False):
        if self.type == None:
            children = [child.get_type() if type(child) is ASTNode else child for child in self.operands]
            self.type = self.operator.typer(children, lval)
        
        return self.type
