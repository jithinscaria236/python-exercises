

## AWS S3 bucket policy restriction


## Steps



- Create an IAM user named "s3-test-user" with below permissons
  ```
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::<s3-bucket-name>/*"
        }
        ]
    }
  ```
- Create an IAM user named "s3-admin-users" with below permissions 
    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "s3:*",
                "Resource": "arn:aws:s3:::*"
            }
        ]
    }
    ```
- Create a S3 Bucket with particular IAM user(s3-admin-users) restriction policy
    ```
    {
        "Version": "2012-10-17",
        "Id": "Policy-S3",
        "Statement": [
            {
                "Sid": "Deny s3 access",
                "Effect": "Deny",
                "Principal": {
                    "AWS": "arn:aws:iam::<aws-account-number>:user/s3-admin-users"
                },
                "Action": "s3:*",
                "Resource": "arn:aws:s3:::<s3-bucket-name>"
            }
        ]
    }
    ```
- Login as s3-admin-users to view the restriction of s3 bucket
  ![aws](/documents/s3-policy.png)
