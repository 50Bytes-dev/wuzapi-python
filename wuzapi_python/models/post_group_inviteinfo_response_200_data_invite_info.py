from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostGroupInviteinfoResponse200DataInviteInfo")


@_attrs_define
class PostGroupInviteinfoResponse200DataInviteInfo:
    """
    Attributes:
        group_name (Union[Unset, str]):  Example: Test Group.
        group_jid (Union[Unset, str]):  Example: 120363312246943103@g.us.
    """

    group_name: Union[Unset, str] = UNSET
    group_jid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_name = self.group_name

        group_jid = self.group_jid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_name is not UNSET:
            field_dict["GroupName"] = group_name
        if group_jid is not UNSET:
            field_dict["GroupJID"] = group_jid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_name = d.pop("GroupName", UNSET)

        group_jid = d.pop("GroupJID", UNSET)

        post_group_inviteinfo_response_200_data_invite_info = cls(
            group_name=group_name,
            group_jid=group_jid,
        )

        post_group_inviteinfo_response_200_data_invite_info.additional_properties = d
        return post_group_inviteinfo_response_200_data_invite_info

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
