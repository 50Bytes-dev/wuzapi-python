import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="HistoryMessage")


@_attrs_define
class HistoryMessage:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the message in the history database Example: 1.
        user_id (Union[Unset, str]): ID of the user who owns this message history Example: abc123def456.
        chat_jid (Union[Unset, str]): WhatsApp JID of the chat where this message was sent/received Example:
            5491155553333@s.whatsapp.net.
        sender_jid (Union[Unset, str]): WhatsApp JID of the user who sent this message Example:
            5491155554444@s.whatsapp.net.
        message_id (Union[Unset, str]): WhatsApp message ID Example: 3EB0C767D26A1B5F7C83.
        timestamp (Union[Unset, datetime.datetime]): Timestamp when the message was sent/received Example:
            2023-12-01T15:30:00Z.
        message_type (Union[Unset, str]): Type of message (text, image, audio, video, document, sticker, contact,
            location, etc.) Example: text.
        text_content (Union[Unset, str]): Text content of the message (for text messages or captions) Example: Hello,
            how are you?.
        media_link (Union[Unset, str]): Link to media file (for media messages) Example:
            https://example.com/media/image123.jpg.
    """

    id: Union[Unset, int] = UNSET
    user_id: Union[Unset, str] = UNSET
    chat_jid: Union[Unset, str] = UNSET
    sender_jid: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    message_type: Union[Unset, str] = UNSET
    text_content: Union[Unset, str] = UNSET
    media_link: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        chat_jid = self.chat_jid

        sender_jid = self.sender_jid

        message_id = self.message_id

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        message_type = self.message_type

        text_content = self.text_content

        media_link = self.media_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if chat_jid is not UNSET:
            field_dict["chat_jid"] = chat_jid
        if sender_jid is not UNSET:
            field_dict["sender_jid"] = sender_jid
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if message_type is not UNSET:
            field_dict["message_type"] = message_type
        if text_content is not UNSET:
            field_dict["text_content"] = text_content
        if media_link is not UNSET:
            field_dict["media_link"] = media_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("user_id", UNSET)

        chat_jid = d.pop("chat_jid", UNSET)

        sender_jid = d.pop("sender_jid", UNSET)

        message_id = d.pop("message_id", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        message_type = d.pop("message_type", UNSET)

        text_content = d.pop("text_content", UNSET)

        media_link = d.pop("media_link", UNSET)

        history_message = cls(
            id=id,
            user_id=user_id,
            chat_jid=chat_jid,
            sender_jid=sender_jid,
            message_id=message_id,
            timestamp=timestamp,
            message_type=message_type,
            text_content=text_content,
            media_link=media_link,
        )

        history_message.additional_properties = d
        return history_message

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
