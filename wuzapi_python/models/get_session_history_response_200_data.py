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
        details (Union[Unset, str]):  Example: History sync request sent.
        timestamp (Union[Unset, int]): Unix timestamp when the sync request was sent Example: 1701432600.
        chat_jid (Union[Unset, str]): The chat JID that was synced (if specified) Example: 5491155553333@s.whatsapp.net.
        message_id (Union[Unset, str]): The message ID used as starting point (if specified) Example:
            3EB0C767D26A1B5F7C83.
        timestamp_param (Union[Unset, str]): The timestamp parameter used as starting point (if specified) Example:
            2023-12-01T15:30:00Z.
        limit (Union[Unset, int]): The limit of messages requested for sync Example: 50.
    """

    details: Union[Unset, str] = UNSET
    timestamp: Union[Unset, int] = UNSET
    chat_jid: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    timestamp_param: Union[Unset, str] = UNSET
    limit: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        timestamp = self.timestamp

        chat_jid = self.chat_jid

        message_id = self.message_id

        timestamp_param = self.timestamp_param

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if chat_jid is not UNSET:
            field_dict["chat_jid"] = chat_jid
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if timestamp_param is not UNSET:
            field_dict["timestamp_param"] = timestamp_param
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        details = d.pop("details", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        chat_jid = d.pop("chat_jid", UNSET)

        message_id = d.pop("message_id", UNSET)

        timestamp_param = d.pop("timestamp_param", UNSET)

        limit = d.pop("limit", UNSET)

        get_session_history_response_200_data = cls(
            details=details,
            timestamp=timestamp,
            chat_jid=chat_jid,
            message_id=message_id,
            timestamp_param=timestamp_param,
            limit=limit,
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
