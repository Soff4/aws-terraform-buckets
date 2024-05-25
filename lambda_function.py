import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3', endpoint_url='http://localhost:4566')
    source_bucket = 's3-start'
    target_bucket = 's3-finish'
    for record in event['Records']:
        key = record['s3']['object']['key']
        copy_source = {'Bucket': source_bucket, 'Key': key}
        s3.copy_object(CopySource=copy_source, Bucket=target_bucket, Key=key)
    return {'statusCode': 200, 'body': 'Файл були скопійовані з достатнім успіхом!'}
