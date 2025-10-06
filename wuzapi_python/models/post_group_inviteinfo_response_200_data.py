from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_group_inviteinfo_response_200_data_invite_info import (
        PostGroupInviteinfoResponse200DataInviteInfo,
    )


T = TypeVar("T", bound="PostGroupInviteinfoResponse200Data")


@_attrs_define
class PostGroupInviteinfoResponse200Data:
    """
    Attributes:
        invite_info (Union[Unset, PostGroupInviteinfoResponse200DataInviteInfo]):
    """

    invite_info: Union[Unset, "PostGroupInviteinfoResponse200DataInviteInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invite_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.invite_info, Unset):
            invite_info = self.invite_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invite_info is not UNSET:
            field_dict["InviteInfo"] = invite_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_group_inviteinfo_response_200_data_invite_info import (
            PostGroupInviteinfoResponse200DataInviteInfo,
        )

        d = dict(src_dict)
        _invite_info = d.pop("InviteInfo", UNSET)
        invite_info: Union[Unset, PostGroupInviteinfoResponse200DataInviteInfo]
        if isinstance(_invite_info, Unset):
            invite_info = UNSET
        else:
            invite_info = PostGroupInviteinfoResponse200DataInviteInfo.from_dict(_invite_info)

        post_group_inviteinfo_response_200_data = cls(
            invite_info=invite_info,
        )

        post_group_inviteinfo_response_200_data.additional_properties = d
        return post_group_inviteinfo_response_200_data

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
