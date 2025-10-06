from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageListListItem")


@_attrs_define
class MessageListListItem:
    """
    Attributes:
        title (Union[Unset, str]):  Example: menu button 1.
        desc (Union[Unset, str]):  Example: long description.
        row_id (Union[Unset, str]):  Example: 1.
    """

    title: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
    row_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        desc = self.desc

        row_id = self.row_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if desc is not UNSET:
            field_dict["desc"] = desc
        if row_id is not UNSET:
            field_dict["RowId"] = row_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        desc = d.pop("desc", UNSET)

        row_id = d.pop("RowId", UNSET)

        message_list_list_item = cls(
            title=title,
            desc=desc,
            row_id=row_id,
        )

        message_list_list_item.additional_properties = d
        return message_list_list_item

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
