from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserS3Config")


@_attrs_define
class CreateUserS3Config:
    """
    Attributes:
        enabled (Union[Unset, bool]): Enable S3 for the user, default is false Example: True.
        endpoint (Union[Unset, str]):  Example: https://s3.amazonaws.com.
        region (Union[Unset, str]):  Example: us-east-1.
        bucket (Union[Unset, str]):  Example: my-bucket.
        access_key (Union[Unset, str]):  Example: 1234567890.
        secret_key (Union[Unset, str]):  Example: 1234567890.
        path_style (Union[Unset, bool]): Enable path style for the user, default is false Example: True.
        public_url (Union[Unset, str]): Public URL for the user Example: https://s3.amazonaws.com.
        media_delivery (Union[Unset, str]): Media delivery type for the user, default is both Example: both.
        retention_days (Union[Unset, int]): Retention days for the user, default is 30 Example: 30.
    """

    enabled: Union[Unset, bool] = UNSET
    endpoint: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    bucket: Union[Unset, str] = UNSET
    access_key: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    path_style: Union[Unset, bool] = UNSET
    public_url: Union[Unset, str] = UNSET
    media_delivery: Union[Unset, str] = UNSET
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

        media_delivery = self.media_delivery

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
            field_dict["accessKey"] = access_key
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if path_style is not UNSET:
            field_dict["pathStyle"] = path_style
        if public_url is not UNSET:
            field_dict["publicURL"] = public_url
        if media_delivery is not UNSET:
            field_dict["mediaDelivery"] = media_delivery
        if retention_days is not UNSET:
            field_dict["retentionDays"] = retention_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        region = d.pop("region", UNSET)

        bucket = d.pop("bucket", UNSET)

        access_key = d.pop("accessKey", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        path_style = d.pop("pathStyle", UNSET)

        public_url = d.pop("publicURL", UNSET)

        media_delivery = d.pop("mediaDelivery", UNSET)

        retention_days = d.pop("retentionDays", UNSET)

        create_user_s3_config = cls(
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

        create_user_s3_config.additional_properties = d
        return create_user_s3_config

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
