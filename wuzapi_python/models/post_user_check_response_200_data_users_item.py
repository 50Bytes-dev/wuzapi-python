from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUserCheckResponse200DataUsersItem")


@_attrs_define
class PostUserCheckResponse200DataUsersItem:
    """
    Attributes:
        is_in_whatsapp (Union[Unset, bool]):  Example: True.
        jid (Union[Unset, str]):  Example: 5491155553934@s.whatsapp.net.
        query (Union[Unset, str]):  Example: 5491155553934.
        verified_name (Union[Unset, str]):  Example: Company Name.
    """

    is_in_whatsapp: Union[Unset, bool] = UNSET
    jid: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    verified_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_in_whatsapp = self.is_in_whatsapp

        jid = self.jid

        query = self.query

        verified_name = self.verified_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_in_whatsapp is not UNSET:
            field_dict["IsInWhatsapp"] = is_in_whatsapp
        if jid is not UNSET:
            field_dict["JID"] = jid
        if query is not UNSET:
            field_dict["Query"] = query
        if verified_name is not UNSET:
            field_dict["VerifiedName"] = verified_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_in_whatsapp = d.pop("IsInWhatsapp", UNSET)

        jid = d.pop("JID", UNSET)

        query = d.pop("Query", UNSET)

        verified_name = d.pop("VerifiedName", UNSET)

        post_user_check_response_200_data_users_item = cls(
            is_in_whatsapp=is_in_whatsapp,
            jid=jid,
            query=query,
            verified_name=verified_name,
        )

        post_user_check_response_200_data_users_item.additional_properties = d
        return post_user_check_response_200_data_users_item

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
