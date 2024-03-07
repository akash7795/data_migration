from data_migration.transformation.expression.expression_tree.nodes.nodes import FunctionNode, LiteralOperandNode, StringLiteralOperandNode, ColumnOperandNode

class NodeFactory():
    @classmethod
    def get_node(cls, type, value, output_column_name=None):
        if type == 'expression':
            return FunctionNode(value, output_column_name)
        elif type == 'literal':
            return StringLiteralOperandNode(value, output_column_name) if isinstance(value, str) else LiteralOperandNode(value, output_column_name)
        elif type == 'column':
            return ColumnOperandNode(value, output_column_name)
