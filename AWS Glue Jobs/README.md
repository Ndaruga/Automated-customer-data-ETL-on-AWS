## Simple ETL on AWS GLue jobs
This is a simple ETL process that dooes the following:
<ol>
  <li> Picks the customer data from an `s3` bucket in `.csv` format.</li>
  <li> Apply mapping transformation and drop columns</li>
  <li> Save the `.csv` file into the `.parquet` file in the same s3 bucket but in a different folder</li>
</ol>

## Prerequisites
<ul>
  <li>S3 bucket</li>
  <li>Create an IAM role for AWS Glue job</li>
  Attach the following `Read` and `Write` policy
  
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::{BUCKET-NAME}/path/to/folder/*"
            ]
        }
    ]
}

  ```
  Replace BUCKET-NAME with the name of your bucket and path/to/folder with the path to the desired folder that contains the files to be read and those to be written after the job has successfully completed running.
  <li>Proceed to configure the ETL job.</li>
  As a precautionary measure to SAVE ON COST,Just before  saving and running the job, <br>
  on the `Job details` tab under `Requested number of workers` reduce the default from 10. This is done to reduce the number of data processing units (DPUs) used to run your ETL job. <br> However, this depends on your workload
  ![image](https://github.com/Ndarugaa/Automated-customer-data-ETL-on-AWS/assets/68260816/97bb4706-23cb-4658-b66a-5e532dc351f0)

</ul>
