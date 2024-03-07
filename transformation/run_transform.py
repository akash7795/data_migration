from data_migration.utils.config_parser import read_config_file
from data_migration.transformation.expression.expression_tree.expression_tree import ExpressionTree

class RunSQLTransform():
    def __init__(self, spark_session, transformation_config_file: str, dataset_ref: str):
        self.transformation_config_file = transformation_config_file
        self.spark_session = spark_session
        self.dataset_ref = dataset_ref

    def _get_xform_expressions(self):
        return read_config_file(self.transformation_config_file)

    def _build_expressions(self):
        """
            Construct SQL expressions based on transformations listed in transformation config file
            Returns a list a SQL expressions
        """
        xform_expressions = self._get_xform_expressions()

        expr_list = []
        for expression in xform_expressions['expressions']:
            expression_tree = ExpressionTree(expression)
            expr_list.append(expression_tree.evaluate())

        return expr_list

    def _build_query(self):
        return ("SELECT\n{sql_expressions}\nFROM {dataset}".format(
                sql_expressions=',\n'.join(self._build_expressions()),
                dataset=self.dataset_ref
            )
        )

    def run(self):
        return self.spark_session.sql(self._build_query())
