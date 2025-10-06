from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGroupInfoResponse200DataParticipantsItem")


@_attrs_define
class GetGroupInfoResponse200DataParticipantsItem:
    """
    Attributes:
        is_admin (Union[Unset, bool]):  Example: True.
        is_super_admin (Union[Unset, bool]):  Example: True.
        jid (Union[Unset, str]):  Example: 5491155554444@s.whatsapp.net.
    """

    is_admin: Union[Unset, bool] = UNSET
    is_super_admin: Union[Unset, bool] = UNSET
    jid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_admin = self.is_admin

        is_super_admin = self.is_super_admin

        jid = self.jid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_admin is not UNSET:
            field_dict["IsAdmin"] = is_admin
        if is_super_admin is not UNSET:
            field_dict["IsSuperAdmin"] = is_super_admin
        if jid is not UNSET:
            field_dict["JID"] = jid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_admin = d.pop("IsAdmin", UNSET)

        is_super_admin = d.pop("IsSuperAdmin", UNSET)

        jid = d.pop("JID", UNSET)

        get_group_info_response_200_data_participants_item = cls(
            is_admin=is_admin,
            is_super_admin=is_super_admin,
            jid=jid,
        )

        get_group_info_response_200_data_participants_item.additional_properties = d
        return get_group_info_response_200_data_participants_item

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
