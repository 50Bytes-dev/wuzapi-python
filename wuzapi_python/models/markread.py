from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Markread")


@_attrs_define
class Markread:
    """
    Attributes:
        id (list[str]):  Example: ['AABBCC11223344', 'DDEEFF55667788'].
        chat (str):  Example: 5491155553934.0:1@s.whatsapp.net.
        sender (Union[Unset, str]):  Example: 5491155553111.0:1@s.whatsapp.net.
    """

    id: list[str]
    chat: str
    sender: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        chat = self.chat

        sender = self.sender

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
                "Chat": chat,
            }
        )
        if sender is not UNSET:
            field_dict["Sender"] = sender

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = cast(list[str], d.pop("Id"))

        chat = d.pop("Chat")

        sender = d.pop("Sender", UNSET)

        markread = cls(
            id=id,
            chat=chat,
            sender=sender,
        )

        markread.additional_properties = d
        return markread

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
