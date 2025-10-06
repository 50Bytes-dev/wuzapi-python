from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupPhoto")


@_attrs_define
class GroupPhoto:
    """
    Attributes:
        group_jid (Union[Unset, str]):  Example: 120362023605733675@g.us.
        image (Union[Unset, str]): Base64 encoded image data with data URL format. Supported format: JPEG! Example:
            data:image/jpeg;base64,Akd9300....
    """

    group_jid: Union[Unset, str] = UNSET
    image: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_jid = self.group_jid

        image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_jid is not UNSET:
            field_dict["GroupJID"] = group_jid
        if image is not UNSET:
            field_dict["Image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_jid = d.pop("GroupJID", UNSET)

        image = d.pop("Image", UNSET)

        group_photo = cls(
            group_jid=group_jid,
            image=image,
        )

        group_photo.additional_properties = d
        return group_photo

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
