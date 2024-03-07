from data_migration.transformation.expression.expression_tree.nodes.node_factory import NodeFactory

class ExpressionParser():
    def __init__(self):
        pass

    def get_nodes(self, expr):
        node_type = expr.get('type', 'column')

        if node_type == 'expression':
            root = NodeFactory.get_node(node_type, expr['operator'], expr.get('output_column_name', None))
            for operand in expr.get('operands', []):
                root.add_child(self.get_nodes(operand))

        else:
            root = NodeFactory.get_node(node_type, expr['value'], expr.get('output_column_name', None))

        return root
