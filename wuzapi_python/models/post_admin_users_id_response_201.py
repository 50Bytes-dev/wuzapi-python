from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="PostAdminUsersIdResponse201")


@_attrs_define
class PostAdminUsersIdResponse201:
    """
    Attributes:
        code (Union[Unset, int]):  Example: 201.
        success (Union[Unset, bool]):  Example: True.
        data (Union[Unset, User]):
    """

    code: Union[Unset, int] = UNSET
    success: Union[Unset, bool] = UNSET
    data: Union[Unset, "User"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        success = self.success

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if success is not UNSET:
            field_dict["success"] = success
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        success = d.pop("success", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, User]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = User.from_dict(_data)

        post_admin_users_id_response_201 = cls(
            code=code,
            success=success,
            data=data,
        )

        post_admin_users_id_response_201.additional_properties = d
        return post_admin_users_id_response_201

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
