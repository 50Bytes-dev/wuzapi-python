from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_user_check_response_200_data_users_item import PostUserCheckResponse200DataUsersItem


T = TypeVar("T", bound="PostUserCheckResponse200Data")


@_attrs_define
class PostUserCheckResponse200Data:
    """
    Attributes:
        users (Union[Unset, list['PostUserCheckResponse200DataUsersItem']]):
    """

    users: Union[Unset, list["PostUserCheckResponse200DataUsersItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["Users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_user_check_response_200_data_users_item import PostUserCheckResponse200DataUsersItem

        d = dict(src_dict)
        users = []
        _users = d.pop("Users", UNSET)
        for users_item_data in _users or []:
            users_item = PostUserCheckResponse200DataUsersItem.from_dict(users_item_data)

            users.append(users_item)

        post_user_check_response_200_data = cls(
            users=users,
        )

        post_user_check_response_200_data.additional_properties = d
        return post_user_check_response_200_data

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
