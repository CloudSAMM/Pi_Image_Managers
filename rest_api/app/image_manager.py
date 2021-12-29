import boto3
import os
import decouple
from fastapi.responses import JSONResponse


class ImageInterface:
    session = boto3.session.Session()
    client = session.client(
        "s3",
        endpoint_url=decouple.config("hostname"),
        aws_access_key_id=decouple.config("access_key_id"),
        aws_secret_access_key=decouple.config("secret_access_key"),
    )

    @classmethod
    def get_images(cls, cam_id: str, prefix: str):
        try:
            objs = cls.client.list_objects(Bucket=cam_id, Prefix=prefix)
            return JSONResponse(cls._format_response(objs), status_code=200)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=401)

    @classmethod
    def _format_response(cls, data):
        content = data.get("Contents", []) or []
        bucket = data.get("Name")
        return {key.get("Key"): f"image/{bucket}/{key.get('Key')}" for key in content}

    @classmethod
    def generate_url(cls, bucket: str, key: str):
        return cls.client.generate_presigned_url(
            "get_object", Params={"Bucket": bucket, "Key": key}
        )

    @staticmethod
    def create_prefix(year: str = None, month: str = str, day: str = None):
        res = ""
        if year:
            res += f"{year}"
        if month and year:
            res += f"-{month}"
        if day and month and year:
            res += f"-{day}"
        return res
