from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessagePoll")


@_attrs_define
class MessagePoll:
    """
    Attributes:
        group (str):  Example: 120363417042313103@g.us.
        header (str):  Example: What's your favorite color.
        options (list[str]): An array of options for the poll.
        id (Union[Unset, str]):  Example: 3EB06F9067F80BAB89FF.
    """

    group: str
    header: str
    options: list[str]
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group = self.group

        header = self.header

        options = self.options

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Group": group,
                "Header": header,
                "Options": options,
            }
        )
        if id is not UNSET:
            field_dict["Id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group = d.pop("Group")

        header = d.pop("Header")

        options = cast(list[str], d.pop("Options"))

        id = d.pop("Id", UNSET)

        message_poll = cls(
            group=group,
            header=header,
            options=options,
            id=id,
        )

        message_poll.additional_properties = d
        return message_poll

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
