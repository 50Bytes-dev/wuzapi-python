from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSessionHistoryResponse200Data")


@_attrs_define
class GetSessionHistoryResponse200Data:
    """
    Attributes:
        details (Union[Unset, str]):  Example: History sync request Sent.
        timestamp (Union[Unset, int]): Unix timestamp when the request was sent Example: 1640995200.
        count (Union[Unset, int]): Number of messages requested for sync Example: 50.
        chat_jid (Union[Unset, str]): JID of the chat being synced Example: 120363313346913103@g.us.
        oldest_msg_id (Union[Unset, str]): ID of the oldest message for sync Example: ABC123DEF456.
        oldest_msg_from_me (Union[Unset, bool]): Whether the oldest message was from the user Example: True.
        oldest_msg_timestamp (Union[Unset, int]): Timestamp of the oldest message in milliseconds Example:
            1640995200000.
    """

    details: Union[Unset, str] = UNSET
    timestamp: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    chat_jid: Union[Unset, str] = UNSET
    oldest_msg_id: Union[Unset, str] = UNSET
    oldest_msg_from_me: Union[Unset, bool] = UNSET
    oldest_msg_timestamp: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        timestamp = self.timestamp

        count = self.count

        chat_jid = self.chat_jid

        oldest_msg_id = self.oldest_msg_id

        oldest_msg_from_me = self.oldest_msg_from_me

        oldest_msg_timestamp = self.oldest_msg_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if count is not UNSET:
            field_dict["count"] = count
        if chat_jid is not UNSET:
            field_dict["chat_jid"] = chat_jid
        if oldest_msg_id is not UNSET:
            field_dict["oldest_msg_id"] = oldest_msg_id
        if oldest_msg_from_me is not UNSET:
            field_dict["oldest_msg_from_me"] = oldest_msg_from_me
        if oldest_msg_timestamp is not UNSET:
            field_dict["oldest_msg_timestamp"] = oldest_msg_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        details = d.pop("details", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        count = d.pop("count", UNSET)

        chat_jid = d.pop("chat_jid", UNSET)

        oldest_msg_id = d.pop("oldest_msg_id", UNSET)

        oldest_msg_from_me = d.pop("oldest_msg_from_me", UNSET)

        oldest_msg_timestamp = d.pop("oldest_msg_timestamp", UNSET)

        get_session_history_response_200_data = cls(
            details=details,
            timestamp=timestamp,
            count=count,
            chat_jid=chat_jid,
            oldest_msg_id=oldest_msg_id,
            oldest_msg_from_me=oldest_msg_from_me,
            oldest_msg_timestamp=oldest_msg_timestamp,
        )

        get_session_history_response_200_data.additional_properties = d
        return get_session_history_response_200_data

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
