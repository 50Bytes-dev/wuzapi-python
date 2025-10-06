from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGroupInvitelinkResponse200Data")


@_attrs_define
class GetGroupInvitelinkResponse200Data:
    """
    Attributes:
        invite_link (Union[Unset, str]):  Example: https://chat.whatsapp.com/HffXhYmzzyJGec61oqMXiz.
    """

    invite_link: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invite_link = self.invite_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invite_link is not UNSET:
            field_dict["InviteLink"] = invite_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invite_link = d.pop("InviteLink", UNSET)

        get_group_invitelink_response_200_data = cls(
            invite_link=invite_link,
        )

        get_group_invitelink_response_200_data.additional_properties = d
        return get_group_invitelink_response_200_data

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
