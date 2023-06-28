import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": [
            "s3://business-etl-pipeline/data/customer_database/customer_csv_files/customer.csv"
        ],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("CustomerID", "string", "CustomerID", "string"),
        ("NameStyle", "string", "NameStyle", "string"),
        ("FirstName", "string", "FirstName", "string"),
        ("MiddleName", "string", "MiddleName", "string"),
        ("LastName", "string", "LastName", "string"),
        ("Suffix", "string", "Suffix", "string"),
        ("CompanyName", "string", "CompanyName", "string"),
        ("SalesPerson", "string", "SalesPerson", "string"),
        ("EmailAddress", "string", "EmailAddress", "string"),
        ("Phone", "string", "Phone", "string"),
        ("PasswordHash", "string", "PasswordHash", "string"),
        ("PasswordSalt", "string", "PasswordSalt", "string"),
        ("rowguid", "string", "rowguid", "string"),
        ("ModifiedDate", "string", "ModifiedDate", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node2,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://business-etl-pipeline/data/customer_database/customer_parquet_files/",
        "partitionKeys": [],
    },
    format_options={"compression": "uncompressed"},
    transformation_ctx="S3bucket_node3",
)

job.commit()
