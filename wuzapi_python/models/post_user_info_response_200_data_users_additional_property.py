from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUserInfoResponse200DataUsersAdditionalProperty")


@_attrs_define
class PostUserInfoResponse200DataUsersAdditionalProperty:
    """
    Attributes:
        devices (Union[Unset, list[str]]):
        picture_id (Union[Unset, str]):
        status (Union[Unset, str]):
        verified_name (Union[None, Unset, str]):
    """

    devices: Union[Unset, list[str]] = UNSET
    picture_id: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    verified_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        devices: Union[Unset, list[str]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices

        picture_id = self.picture_id

        status = self.status

        verified_name: Union[None, Unset, str]
        if isinstance(self.verified_name, Unset):
            verified_name = UNSET
        else:
            verified_name = self.verified_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["Devices"] = devices
        if picture_id is not UNSET:
            field_dict["PictureID"] = picture_id
        if status is not UNSET:
            field_dict["Status"] = status
        if verified_name is not UNSET:
            field_dict["VerifiedName"] = verified_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        devices = cast(list[str], d.pop("Devices", UNSET))

        picture_id = d.pop("PictureID", UNSET)

        status = d.pop("Status", UNSET)

        def _parse_verified_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        verified_name = _parse_verified_name(d.pop("VerifiedName", UNSET))

        post_user_info_response_200_data_users_additional_property = cls(
            devices=devices,
            picture_id=picture_id,
            status=status,
            verified_name=verified_name,
        )

        post_user_info_response_200_data_users_additional_property.additional_properties = d
        return post_user_info_response_200_data_users_additional_property

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
