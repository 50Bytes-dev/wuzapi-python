from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserContactsResponse200DataAdditionalProperty")


@_attrs_define
class GetUserContactsResponse200DataAdditionalProperty:
    """
    Attributes:
        business_name (Union[Unset, str]):
        first_name (Union[Unset, str]):
        found (Union[Unset, bool]):  Example: True.
        full_name (Union[Unset, str]):
        push_name (Union[Unset, str]):  Example: FOP2.
    """

    business_name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    found: Union[Unset, bool] = UNSET
    full_name: Union[Unset, str] = UNSET
    push_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_name = self.business_name

        first_name = self.first_name

        found = self.found

        full_name = self.full_name

        push_name = self.push_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_name is not UNSET:
            field_dict["BusinessName"] = business_name
        if first_name is not UNSET:
            field_dict["FirstName"] = first_name
        if found is not UNSET:
            field_dict["Found"] = found
        if full_name is not UNSET:
            field_dict["FullName"] = full_name
        if push_name is not UNSET:
            field_dict["PushName"] = push_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_name = d.pop("BusinessName", UNSET)

        first_name = d.pop("FirstName", UNSET)

        found = d.pop("Found", UNSET)

        full_name = d.pop("FullName", UNSET)

        push_name = d.pop("PushName", UNSET)

        get_user_contacts_response_200_data_additional_property = cls(
            business_name=business_name,
            first_name=first_name,
            found=found,
            full_name=full_name,
            push_name=push_name,
        )

        get_user_contacts_response_200_data_additional_property.additional_properties = d
        return get_user_contacts_response_200_data_additional_property

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
