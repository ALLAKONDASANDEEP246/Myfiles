import boto3

#create an object for s3 service
s3_client = boto3.client('s3', 
                         aws_access_key_id= "accesskey",
                         aws_secret_access_key= "secretkey")

# #creation of bucket
# response = s3_client.create_bucket(
#     Bucket='',
#     CreateBucketConfiguration={
#         'LocationConstraint': ''
#     },

    
# )

# print(response)

# #upload a file to s3 bucket
# response = s3_client.put_object(
#     Body=open("index.py", "r").read(),
#     Bucket='x',
#     Key='index.py
# )

# print(response)

#Download a file to local system
response = s3_client.object(
    Bucket='',
    Key='index.py'
)

print(response)