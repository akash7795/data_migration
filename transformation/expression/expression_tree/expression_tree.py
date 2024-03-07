from data_migration.transformation.expression.parser.expression_parser import ExpressionParser

class ExpressionTree():
    def __init__(self, expression_dict):
        self.root = ExpressionParser().get_nodes(expression_dict)

    def evaluate(self):
        return self.root.evaluate()
