from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSessionStatusResponse200Data")


@_attrs_define
class GetSessionStatusResponse200Data:
    """
    Attributes:
        connected (Union[Unset, bool]):  Example: True.
        logged_in (Union[Unset, bool]):  Example: True.
    """

    connected: Union[Unset, bool] = UNSET
    logged_in: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connected = self.connected

        logged_in = self.logged_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connected is not UNSET:
            field_dict["connected"] = connected
        if logged_in is not UNSET:
            field_dict["loggedIn"] = logged_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connected = d.pop("connected", UNSET)

        logged_in = d.pop("loggedIn", UNSET)

        get_session_status_response_200_data = cls(
            connected=connected,
            logged_in=logged_in,
        )

        get_session_status_response_200_data.additional_properties = d
        return get_session_status_response_200_data

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
