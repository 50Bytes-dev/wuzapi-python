from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_list_list_item import MessageListListItem


T = TypeVar("T", bound="MessageList")


@_attrs_define
class MessageList:
    """
    Attributes:
        phone (str):  Example: 5521971532700.
        button_text (str):  Example: Click Here.
        desc (str):  Example: This is a list.
        top_text (str):  Example: This is a list.
        list_ (list['MessageListListItem']):
        footer_text (Union[Unset, str]):  Example: This is a footer text.
    """

    phone: str
    button_text: str
    desc: str
    top_text: str
    list_: list["MessageListListItem"]
    footer_text: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        button_text = self.button_text

        desc = self.desc

        top_text = self.top_text

        list_ = []
        for list_item_data in self.list_:
            list_item = list_item_data.to_dict()
            list_.append(list_item)

        footer_text = self.footer_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Phone": phone,
                "ButtonText": button_text,
                "Desc": desc,
                "TopText": top_text,
                "List": list_,
            }
        )
        if footer_text is not UNSET:
            field_dict["FooterText"] = footer_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_list_list_item import MessageListListItem

        d = dict(src_dict)
        phone = d.pop("Phone")

        button_text = d.pop("ButtonText")

        desc = d.pop("Desc")

        top_text = d.pop("TopText")

        list_ = []
        _list_ = d.pop("List")
        for list_item_data in _list_:
            list_item = MessageListListItem.from_dict(list_item_data)

            list_.append(list_item)

        footer_text = d.pop("FooterText", UNSET)

        message_list = cls(
            phone=phone,
            button_text=button_text,
            desc=desc,
            top_text=top_text,
            list_=list_,
            footer_text=footer_text,
        )

        message_list.additional_properties = d
        return message_list

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
