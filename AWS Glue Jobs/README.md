## Simple ETL on AWS GLue jobs
This is a simple ETL process that does the following:
<ol>
  <li> Picks the customer data from an <strong>s3</strong> bucket in <strong>.csv</strong> format.</li>
  <li> Apply mapping transformation and drop columns</li>
  <li> Save the <strong>.csv</strong> file into the <strong>.parquet</strong> file in the same s3 bucket but in a different folder</li>
</ol>

## Prerequisites
<ul>
  <li>S3 bucket</li>
  <li>Create an IAM role for AWS Glue job</li>
  Attach the following <strong>Read</strong> and <strong>Write</strong> policy
  
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
  As a precautionary measure to SAVE ON COST, Just before  <strong>save</strong> and <strong>run</strong> the job, <br>
  on the <strong>Job details</strong> tab under <strong>Requested number of workers</strong> reduce the default from 10. This is done to reduce the number of data processing units (DPUs) used to run your ETL job. <br><br>

  ![image](https://github.com/Ndarugaa/Automated-customer-data-ETL-on-AWS/assets/68260816/20f75abb-74d9-4168-8f85-6fa2a8ec14a1)

  **However, this depends on the workload**
