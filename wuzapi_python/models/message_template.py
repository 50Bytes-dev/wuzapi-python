from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_template_buttons_item import MessageTemplateButtonsItem
    from ..models.message_template_context_info import MessageTemplateContextInfo


T = TypeVar("T", bound="MessageTemplate")


@_attrs_define
class MessageTemplate:
    """
    Attributes:
        phone (str):  Example: 5491155553935.
        content (str):  Example: Message title.
        footer (Union[Unset, str]):  Example: Text below title, above buttons.
        buttons (Union[Unset, list['MessageTemplateButtonsItem']]):  Example: [{'DisplayText': 'Yes', 'Type':
            'quickreply'}, {'DisplayText': 'No', 'Type': 'quickreply'}, {'DisplayText': 'Visit Site', 'Type': 'url', 'Url':
            'https://www.fop2.com'}, {'DisplayText': 'Callme', 'Type': 'call', 'PhoneNumber': '1155553934'}].
        id (Union[Unset, str]):  Example: ABCDABCD1234.
        context_info (Union[Unset, MessageTemplateContextInfo]):
    """

    phone: str
    content: str
    footer: Union[Unset, str] = UNSET
    buttons: Union[Unset, list["MessageTemplateButtonsItem"]] = UNSET
    id: Union[Unset, str] = UNSET
    context_info: Union[Unset, "MessageTemplateContextInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        content = self.content

        footer = self.footer

        buttons: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.buttons, Unset):
            buttons = []
            for buttons_item_data in self.buttons:
                buttons_item = buttons_item_data.to_dict()
                buttons.append(buttons_item)

        id = self.id

        context_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context_info, Unset):
            context_info = self.context_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Phone": phone,
                "Content": content,
            }
        )
        if footer is not UNSET:
            field_dict["Footer"] = footer
        if buttons is not UNSET:
            field_dict["Buttons"] = buttons
        if id is not UNSET:
            field_dict["Id"] = id
        if context_info is not UNSET:
            field_dict["ContextInfo"] = context_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_template_buttons_item import MessageTemplateButtonsItem
        from ..models.message_template_context_info import MessageTemplateContextInfo

        d = dict(src_dict)
        phone = d.pop("Phone")

        content = d.pop("Content")

        footer = d.pop("Footer", UNSET)

        buttons = []
        _buttons = d.pop("Buttons", UNSET)
        for buttons_item_data in _buttons or []:
            buttons_item = MessageTemplateButtonsItem.from_dict(buttons_item_data)

            buttons.append(buttons_item)

        id = d.pop("Id", UNSET)

        _context_info = d.pop("ContextInfo", UNSET)
        context_info: Union[Unset, MessageTemplateContextInfo]
        if isinstance(_context_info, Unset):
            context_info = UNSET
        else:
            context_info = MessageTemplateContextInfo.from_dict(_context_info)

        message_template = cls(
            phone=phone,
            content=content,
            footer=footer,
            buttons=buttons,
            id=id,
            context_info=context_info,
        )

        message_template.additional_properties = d
        return message_template

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
