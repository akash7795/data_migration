class DatasetUtils():

    @classmethod
    def read_dataset(cls, spark_session, data_path):
        return spark_session.read.parquet(data_path)

    @classmethod
    def get_dataset_ref(cls, spark_session, data_path):
        #read dataset
        df = cls.read_dataset(spark_session, data_path)

        #create ref to dataset for SQL transform step
        from uuid import uuid4
        dataset_ref = str(uuid4()).replace('-', '_')
        df.createOrReplaceTempView(dataset_ref)

        return dataset_ref

    @classmethod
    def write_dataset(cls, df, data_path):
        return df.write.parquet(data_path)
