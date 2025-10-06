from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProxyConfig")


@_attrs_define
class UserProxyConfig:
    """
    Attributes:
        enabled (Union[Unset, bool]):  Example: True.
        proxy_url (Union[Unset, str]):  Example: https://serverproxy.com:9080.
    """

    enabled: Union[Unset, bool] = UNSET
    proxy_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        proxy_url = self.proxy_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if proxy_url is not UNSET:
            field_dict["proxy_url"] = proxy_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        proxy_url = d.pop("proxy_url", UNSET)

        user_proxy_config = cls(
            enabled=enabled,
            proxy_url=proxy_url,
        )

        user_proxy_config.additional_properties = d
        return user_proxy_config

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
