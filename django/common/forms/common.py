import os
import uuid
import hashlib

from django import forms

from core.aws import aws, S3
from core.environment import env
from common.models import StoredFile


class StoredFileAdminForm(forms.ModelForm):
    file = forms.FileField(required=True)

    class Meta:
        model = StoredFile
        exclude = ("name", "path", "hash", "ext", "uploader_type", "uploader_id", "expire_at")
        # fields = "__all__"

    def save(self, commit=True):
        instance = super().save(commit=False)

        uploaded_file = self.cleaned_data['file']
        uploaded_file_ext = os.path.splitext(uploaded_file.name)[1]
        s3_file_name = str(uuid.uuid4())
        s3_file_path = f"static/stored-file/{s3_file_name}{uploaded_file_ext}"

        hasher = hashlib.md5()
        uploaded_file.seek(0)
        while chunk := uploaded_file.read(8192):
            hasher.update(chunk)
        uploaded_file.seek(0)

        s3 = S3(aws.session)
        s3.upload_fileobj(
            file=uploaded_file,
            bucket_name=env.get("AWS_BUCKET_NAME"),
            key=s3_file_path,
            ext=uploaded_file_ext,
        )

        instance.name = s3_file_name
        instance.ext = uploaded_file_ext
        instance.path = s3_file_path
        instance.hash = hasher.hexdigest()

        if commit:
            instance.save()
        return instance
