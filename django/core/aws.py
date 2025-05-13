# -*- coding: utf-8 -*-

import os
import boto3
import botocore.session

from core.environment import env

from typing import Literal, Optional, BinaryIO


class Aws:
    """
    A class for handling AWS operations such as creating and importing credentials.

    :param access_key: Access key of the AWS user credentials.
    :param secret_key: Secret key of the AWS user credentials.
    :param region: Region for the AWS services to be used.
    """
    REGION_LITERAL = Literal[
        "af-south-1", "ap-east-1", "ap-northeast-1", "ap-northeast-2", "ap-northeast-3", "ap-south-1", "ap-southeast-1",
        "ap-southeast-2", "ap-southeast-3", "ca-central-1", "cn-north-1", "cn-northwest-1", "EU", "eu-central-1",
        "eu-north-1", "eu-south-1", "eu-west-1", "eu-west-2", "eu-west-3", "me-south-1", "sa-east-1", "us-east-2",
        "us-gov-east-1", "us-gov-west-1", "us-west-1", "us-west-2"
    ]

    def __init__(self, access_key: Optional[str] = None, secret_key: Optional[str] = None,
                 region: REGION_LITERAL = "ap-northeast-2") -> None:
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region

        if self.access_key is None and self.secret_key is None:
            self.session = boto3.Session(
                botocore_session=botocore.session.get_session(),
                region_name=self.region
            )
        else:
            self.session = boto3.Session(
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
                region_name=self.region
            )


aws = Aws(
    access_key=env.get("AWS_ACCESS_KEY"),
    secret_key=env.get("AWS_SECRET_KEY"),
    region=env.get("AWS_REGION")
)


class S3:
    COMMON_MIME_TYPE = {
        ".aac": "audio/aac",
        ".abw": "application/x-abiword",
        ".arc": "application/x-freearc",
        ".avi": "video/x-msvideo",
        ".avif": "image/avif",
        ".azw": "application/vnd.amazon.ebook",
        ".bin": "application/octet-stream",
        ".bmp": "image/bmp",
        ".bz": "application/x-bzip",
        ".bz2": "application/x-bzip2",
        ".cda": "application/x-cdf",
        ".csh": "application/x-csh",
        ".css": "text/css",
        ".csv": "text/csv",
        ".doc": "application/msword",
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".eot": "application/vnd.ms-fontobject",
        ".epub": "application/epub+zip",
        ".gz": "application/gzip",
        ".gif": "image/gif",
        ".htm": "text/html",
        ".html": "text/html",
        ".ico": "image/x-icon",
        ".jar": "application/java-archive",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".js": "application/javascript",
        ".json": "application/json",
        ".jsonld": "application/ld+json",
        ".m3u8": "application/vnd.apple.mpegurl",  # not common
        ".mid": "audio/x-midi",
        ".midi": "audio/x-midi",
        ".mjs": "text/javascript",
        ".mp3": "audio/mpeg",
        ".mp4": "video/mp4",
        ".mpd": "application/dash+xml",  # not common
        ".mpeg": "video/mpeg",
        ".mpkg": "application/vnd.apple.installer+xml",
        ".odp": "application/vnd.oasis.opendocument.presentation",
        ".ods": "application/vnd.oasis.opendocument.spreadsheet",
        ".odt": "application/vnd.oasis.opendocument.text",
        ".oga": "audio/ogg",
        ".ogv": "video/ogg",
        ".ogx": "application/ogg",
        ".opus": "audio/opus",
        ".otf": "font/otf",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".php": "application/x-httpd-php",
        ".ppt": "application/vnd.ms-powerpoint",
        ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ".rar": "application/vnd.rar",
        ".rtf": "application/rtf",
        ".sh": "application/x-sh",
        ".svg": "image/svg+xml",
        ".tar": "application/x-tar",
        ".tif": "image/tiff",
        ".tiff": "image/tiff",
        ".ts": "video/mp2t",
        ".ttf": "font/ttf",
        ".txt": "text/plain",
        ".vsd": "application/vnd.visio",
        ".wav": "audio/wav",
        ".weba": "audio/webm",
        ".webm": "video/webm",
        ".webp": "image/webp",
        ".woff": "font/woff",
        ".woff2": "font/woff2",
        ".xhtml": "application/xhtml+xml",
        ".xls": "application/vnd.ms-excel",
        ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ".xml": "application/xml",
        ".xul": "application/vnd.mozilla.xul+xml",
        ".zip": "application/zip",
        ".3gp": "video/3gpp",
        ".3g2": "video/3gpp2",
        ".7z": "application/x-7z-compressed"
    }

    def __init__(self, session: boto3.Session, endpoint_url: Optional[str] = None):
        self.session = session
        self.client = session.client('s3', endpoint_url=endpoint_url)

    def upload_fileobj(self, bucket_name: str, file: BinaryIO, key: str, ext: str,
                       extra_args: Optional[dict] = None) -> None:
        if extra_args is None:
            extra_args = {}

        if ext in S3.COMMON_MIME_TYPE:
            if "ContentType" not in extra_args:
                extra_args.update({"ContentType": S3.COMMON_MIME_TYPE[ext]})

        self.client.upload_fileobj(
            Fileobj=file,
            Bucket=bucket_name,
            Key=key,
            ExtraArgs=extra_args
        )

__all__ = ["aws", "S3"]
