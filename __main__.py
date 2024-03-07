from data_migration.transformation.run_transform import RunSQLTransform
from data_migration.utils.dataframe_utils import DatasetUtils

config_file_path = 'transformations.json'
input_path = 'input.parquet'
output_path = 'output.parquet'

DatasetUtils.write_dataset(
    RunSQLTransform(spark, config_file_path, DatasetUtils.get_dataset_ref(spark, input_path)).run(),
    output_path
)
