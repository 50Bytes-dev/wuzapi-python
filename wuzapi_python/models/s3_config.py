from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.s3_config_media_delivery import S3ConfigMediaDelivery
from ..types import UNSET, Unset

T = TypeVar("T", bound="S3Config")


@_attrs_define
class S3Config:
    """
    Attributes:
        enabled (Union[Unset, bool]): Whether S3 storage is enabled Example: True.
        endpoint (Union[Unset, str]): S3 endpoint URL (leave empty for AWS S3) Example: https://s3.amazonaws.com.
        region (Union[Unset, str]): S3 region Example: us-east-1.
        bucket (Union[Unset, str]): S3 bucket name Example: my-whatsapp-media.
        access_key (Union[Unset, str]): S3 access key ID Example: AKIAIOSFODNN7EXAMPLE.
        secret_key (Union[Unset, str]): S3 secret access key Example: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY.
        path_style (Union[Unset, bool]): Use path-style URLs (required for MinIO)
        public_url (Union[Unset, str]): Custom public URL for accessing files (optional, for CDN) Example:
            https://cdn.example.com.
        media_delivery (Union[Unset, S3ConfigMediaDelivery]): Media delivery method Example: both.
        retention_days (Union[Unset, int]): Number of days to retain files (0 for no expiration) Example: 30.
    """

    enabled: Union[Unset, bool] = UNSET
    endpoint: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    bucket: Union[Unset, str] = UNSET
    access_key: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    path_style: Union[Unset, bool] = UNSET
    public_url: Union[Unset, str] = UNSET
    media_delivery: Union[Unset, S3ConfigMediaDelivery] = UNSET
    retention_days: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        endpoint = self.endpoint

        region = self.region

        bucket = self.bucket

        access_key = self.access_key

        secret_key = self.secret_key

        path_style = self.path_style

        public_url = self.public_url

        media_delivery: Union[Unset, str] = UNSET
        if not isinstance(self.media_delivery, Unset):
            media_delivery = self.media_delivery.value

        retention_days = self.retention_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if region is not UNSET:
            field_dict["region"] = region
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if access_key is not UNSET:
            field_dict["access_key"] = access_key
        if secret_key is not UNSET:
            field_dict["secret_key"] = secret_key
        if path_style is not UNSET:
            field_dict["path_style"] = path_style
        if public_url is not UNSET:
            field_dict["public_url"] = public_url
        if media_delivery is not UNSET:
            field_dict["media_delivery"] = media_delivery
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        region = d.pop("region", UNSET)

        bucket = d.pop("bucket", UNSET)

        access_key = d.pop("access_key", UNSET)

        secret_key = d.pop("secret_key", UNSET)

        path_style = d.pop("path_style", UNSET)

        public_url = d.pop("public_url", UNSET)

        _media_delivery = d.pop("media_delivery", UNSET)
        media_delivery: Union[Unset, S3ConfigMediaDelivery]
        if isinstance(_media_delivery, Unset):
            media_delivery = UNSET
        else:
            media_delivery = S3ConfigMediaDelivery(_media_delivery)

        retention_days = d.pop("retention_days", UNSET)

        s3_config = cls(
            enabled=enabled,
            endpoint=endpoint,
            region=region,
            bucket=bucket,
            access_key=access_key,
            secret_key=secret_key,
            path_style=path_style,
            public_url=public_url,
            media_delivery=media_delivery,
            retention_days=retention_days,
        )

        s3_config.additional_properties = d
        return s3_config

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
