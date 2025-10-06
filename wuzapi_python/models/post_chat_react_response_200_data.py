from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostChatReactResponse200Data")


@_attrs_define
class PostChatReactResponse200Data:
    """
    Attributes:
        details (Union[Unset, str]):  Example: Sent.
        id (Union[Unset, str]):  Example: 3EB06F9067F80BAB89FF.
        timestamp (Union[Unset, str]):  Example: 2022-05-10T12:49:08-03:00.
    """

    details: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        id = self.id

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["Details"] = details
        if id is not UNSET:
            field_dict["Id"] = id
        if timestamp is not UNSET:
            field_dict["Timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        details = d.pop("Details", UNSET)

        id = d.pop("Id", UNSET)

        timestamp = d.pop("Timestamp", UNSET)

        post_chat_react_response_200_data = cls(
            details=details,
            id=id,
            timestamp=timestamp,
        )

        post_chat_react_response_200_data.additional_properties = d
        return post_chat_react_response_200_data

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
