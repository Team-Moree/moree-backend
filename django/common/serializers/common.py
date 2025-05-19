import os
import hashlib
import uuid
from rest_framework import serializers

from core.aws import aws, S3
from core.environment import env

from common.models import (
    StoredFile,
    StoredFilesGroup
)
from common.enums import UploaderTypeEnum


class StoredFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)

    class Meta:
        model = StoredFile
        read_only_fields = ("name", "ext", "path")
        exclude = ("expire_at", "hash", "uploader_type", "uploader_id", "status")

    def create(self, validated_data):
        uploaded_file = validated_data.pop("file")
        uploaded_file_ext = os.path.splitext(uploaded_file.name)[1]
        s3_file_name = str(uuid.uuid4())
        s3_file_path = f"static/stored-file/{s3_file_name}{uploaded_file_ext}"

        hasher = hashlib.md5()
        uploaded_file.seek(0)
        for chunk in uploaded_file.chunks():
            hasher.update(chunk)
        uploaded_file.seek(0)

        s3 = S3(aws.session)
        s3.upload_fileobj(
            file=uploaded_file,
            bucket_name=env.get("AWS_BUCKET_NAME"),
            key=s3_file_path,
            ext=uploaded_file_ext,
        )

        return StoredFile.objects.create(
            name=s3_file_name,
            ext=uploaded_file_ext,
            path=s3_file_path,
            hash=hasher.hexdigest(),
            uploader_type=UploaderTypeEnum.USER.value,
            uploader_id=self.context["request"].user.id,
        )


class StoredFilesGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoredFilesGroup
        read_only_fields = ("status",)
        exclude = ("status",)