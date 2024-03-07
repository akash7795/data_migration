from abc import ABC, abstractmethod
from data_migration.transformation.sql.functions import get_function

class Node(ABC):

    def __init__(self):
        self.children = None

    @abstractmethod
    def evaluate(self):
        raise NotImplementedError("Subclass must implement evaluate method")

    def add_child(self, node):
        if self.children is None:
            self.children = [node]
        else:
            self.children.append(node)


class FunctionNode(Node):
    def __init__(self, function_name: str, output_column_name: str):
        super(FunctionNode, self).__init__()
        self.function = function_name
        self.output_column_name = output_column_name

    def evaluate(self):
        operator = get_function(self.function)
        operands = []
        for node in self.children:
            operands.append(node.evaluate())

        expr = operator(*operands)
        return "({}) AS {}".format(expr, self.output_column_name) if self.output_column_name else expr
        # return operator(*operands)


class LiteralOperandNode(Node):
    def __init__(self, value: str, output_column_name: str):
        super(LiteralOperandNode, self).__init__()
        self.value = value
        self.output_column_name = output_column_name

    def evaluate(self):
        return "{} AS {}".format(self.value, self.output_column_name) if self.output_column_name else self.value


class StringLiteralOperandNode(LiteralOperandNode):
    def __init__(self, value: str, output_column_name: str):
        super(StringLiteralOperandNode, self).__init__(value, output_column_name)

    def evaluate(self):
        expr = "\"{}\"".format(self.value)
        return "{} AS {}".format(expr, self.output_column_name) if self.output_column_name else expr


class ColumnOperandNode(Node):
    def __init__(self, value: str, output_column_name: str):
        super(ColumnOperandNode, self).__init__()
        self.value = value
        self.output_column_name = output_column_name

    def evaluate(self):
        return "{} AS {}".format(self.value, self.output_column_name) if self.output_column_name else self.value
