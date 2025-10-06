from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostGroupPhotoResponse200Data")


@_attrs_define
class PostGroupPhotoResponse200Data:
    """
    Attributes:
        details (Union[Unset, str]):  Example: Group Photo set successfully.
        picture_id (Union[Unset, str]):  Example: 1222332123.
    """

    details: Union[Unset, str] = UNSET
    picture_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        picture_id = self.picture_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["Details"] = details
        if picture_id is not UNSET:
            field_dict["PictureID"] = picture_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        details = d.pop("Details", UNSET)

        picture_id = d.pop("PictureID", UNSET)

        post_group_photo_response_200_data = cls(
            details=details,
            picture_id=picture_id,
        )

        post_group_photo_response_200_data.additional_properties = d
        return post_group_photo_response_200_data

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
