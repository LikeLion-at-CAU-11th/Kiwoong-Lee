from rest_framework import serializers
from .models import Post
from rest_framework import serializers
from config.settings import AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME

import boto3

VALID_IMAGE_EXTENSIONS = [ "jpg", "jpeg", "png", "gif" ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ["writer","content"]
        fields = '__all__'

    def validate(self, data): 
        image = data.get('thumbnail')

        if not image.name.split('.')[-1].lower() in VALID_IMAGE_EXTENSIONS:
            serializers.ValidationError("Not an Image File")
        s3 = boto3.client('s3',
                aws_access_key_id = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                region_name = AWS_REGION)
        try:
            s3.upload_fileobj(image, AWS_STORAGE_BUCKET_NAME, image.name)
            img_url = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{image.name}"
            data['thumbnail'] = img_url
            return data
        except:
            raise serializers.ValidationError("InValid Image File")
        