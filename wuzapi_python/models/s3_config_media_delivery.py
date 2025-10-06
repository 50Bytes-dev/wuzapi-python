from enum import Enum


class S3ConfigMediaDelivery(str, Enum):
    BASE64 = "base64"
    BOTH = "both"
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
