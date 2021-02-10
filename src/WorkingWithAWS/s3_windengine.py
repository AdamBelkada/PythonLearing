
import hashlib
import boto3
from botocore.exceptions import ClientError
import os
import sys
import argparse

class S3Upload():

    def __init__(self, args, s3_client):
        self.argument = args
        self.s3_client = s3_client
        self.file_path, self.bucket, self.key = self.get_args()

    def get_args(self):
        args = self.argument.split("::")
        if len(args) > 3:
            raise Exception("S3Upload Hook: Max arguments 3")
        elif len(args) < 2:
            raise Exception("S3Upload Hook: Min arguments 2")
        elif len(args) == 3:
            self.file_path, self.bucket, self.key = args
        else:
            self.key = None
            self.file_path, self.bucket = args
        return self.file_path, self.bucket, self.key


    def is_new(self, file_path, bucket, key):
        """
        :return: return True if the file doesn't exist in the bucket or if it's different from the local file
        """
        digest = hashlib.md5()
        digest.update(open(file_path, 'rb').read())
        local_file_digest = digest.hexdigest()
        try:
            s3_object = self.s3_client.get_object(
                Bucket=bucket,
                Key=key
            )
            s3_object_digest = s3_object['ResponseMetadata'][
                                   'HTTPHeaders']['etag'][1:-1]
            if local_file_digest == s3_object_digest:
                return False
            else:
                return True
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchKey':
                return True
            else:
                raise

    def upload_directory(self):

        all_files = []

        for root, dirs, files in os.walk(self.file_path):
            all_files += [os.path.join(root, f) for f in files]

        for filename in all_files:

            if self.key:
                object_key = os.path.join(self.key, os.path.relpath(filename, self.file_path))
            else:
                object_key = os.path.basename(filename)
            is_new = self.is_new(filename, self.bucket, object_key)
            if is_new:
                print("... Uploading '%s' to s3 bucket '%s'" % (filename, os.path.join(self.bucket, object_key)))
                with open(filename) as data:
                    self.s3_client.put_object(
                        Bucket=self.bucket,
                        Key=object_key,
                        Body=data.read()
                    )

    def upload_file(self):
        with open(self.file_path) as data:
            if self.key:
                object_key = self.key
            else:
                object_key = self.file_path

            is_new = self.is_new(self.file_path, self.bucket, object_key)
            if is_new:
                print("... Uploading '%s' to s3 bucket '%s'" % (self.file_path, os.path.join(self.bucket, object_key)))
                self.s3_client.put_object(
                    Bucket=self.bucket,
                    Key=object_key,
                    Body=data.read()
                )

    def run(self):
        """
        !s3_upload templates/*::edfred-edfre-sbx-s3-eu-west-1-systemteam-pi2aws::v2/templates/*
        """
        if os.path.isfile(self.file_path):
            self.upload_file()
        elif os.path.isdir(self.file_path):
            self.upload_directory()
        else:
            raise ValueError('src_dir %r not found.' % self.file_path)


def role_arn_to_session(role):
    """
    Usage :
        session = role_arn_to_session(
            RoleArn='arn:aws:iam::012345678901:role/example-role',
            RoleSessionName='ExampleSessionName')
        client = session.client('sqs')
    """
    client = boto3.client('sts')
    response = client.assume_role(
        RoleArn=role,
        RoleSessionName='S3UploadRoleSession',
        DurationSeconds=900
    )
    return boto3.Session(
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken'])


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Smart files uploading to s3')
    parser.add_argument('--role', type=str, nargs='?',
                        help='role to assume', required=False)
    parser.add_argument('--object',
                        help='sum the integers (default: find the max)', required=True)

    args = parser.parse_args(sys.argv[1:])
    s3_client = boto3.client("s3")
    if args.role:
        boto_session = role_arn_to_session(args.role)
        s3_client = boto_session.client("s3")

    s3_upload = S3Upload(args=args.object, s3_client=s3_client)
    s3_upload.run()