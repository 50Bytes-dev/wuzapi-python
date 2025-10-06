from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSessionS3ConfigResponse200Data")


@_attrs_define
class PostSessionS3ConfigResponse200Data:
    """
    Attributes:
        details (Union[Unset, str]):  Example: S3 configuration saved successfully.
        enabled (Union[Unset, bool]):  Example: True.
    """

    details: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["Details"] = details
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        details = d.pop("Details", UNSET)

        enabled = d.pop("Enabled", UNSET)

        post_session_s3_config_response_200_data = cls(
            details=details,
            enabled=enabled,
        )

        post_session_s3_config_response_200_data.additional_properties = d
        return post_session_s3_config_response_200_data

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
