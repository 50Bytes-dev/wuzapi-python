from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUserAvatarResponse200Data")


@_attrs_define
class PostUserAvatarResponse200Data:
    """
    Attributes:
        url (Union[Unset, str]):  Example:
            https://pps.whatsapp.net/v/t61.24694-24/227295214_112447507729487_4643695328050510566_n.jpg?stp=dst-
            jpg_s96x96&ccb=11-4&oh=ja432434a91e8f41d86d341bx889c217&oe=543222A4.
        id (Union[Unset, str]):  Example: 1645308319.
        type_ (Union[Unset, str]):  Example: preview.
        direct_path (Union[Unset, str]):  Example:
            /v/t61.24694-24/227295214_112447507729487_4643695328050510566_n.jpg?stp=dst-
            jpg_s96x96&ccb=11-4&oh=ja432434a91e8f41d86d341ba889c217&oe=543222A4.
    """

    url: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    direct_path: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        id = self.id

        type_ = self.type_

        direct_path = self.direct_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if direct_path is not UNSET:
            field_dict["direct_path"] = direct_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        direct_path = d.pop("direct_path", UNSET)

        post_user_avatar_response_200_data = cls(
            url=url,
            id=id,
            type_=type_,
            direct_path=direct_path,
        )

        post_user_avatar_response_200_data.additional_properties = d
        return post_user_avatar_response_200_data

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
