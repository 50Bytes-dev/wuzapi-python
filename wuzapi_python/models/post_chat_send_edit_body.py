from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostChatSendEditBody")


@_attrs_define
class PostChatSendEditBody:
    """
    Attributes:
        id (str): The ID of the message to edit Example: 90B2F8B13FAC8A9CF6B06E99C7834DC5.
        phone (str): The WhatsApp number or JID (use 'me:' prefix if your own message) Example: 5491122223333.
        body (str): New message content Example: This is the updated message.
    """

    id: str
    phone: str
    body: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        phone = self.phone

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Id": id,
                "Phone": phone,
                "Body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("Id")

        phone = d.pop("Phone")

        body = d.pop("Body")

        post_chat_send_edit_body = cls(
            id=id,
            phone=phone,
            body=body,
        )

        post_chat_send_edit_body.additional_properties = d
        return post_chat_send_edit_body

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
