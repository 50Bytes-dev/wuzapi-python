from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSessionConnectResponse200Data")


@_attrs_define
class PostSessionConnectResponse200Data:
    """
    Attributes:
        details (Union[Unset, str]):  Example: Connected!.
        events (Union[Unset, str]):  Example: Message.
        jid (Union[Unset, str]):  Example: 5491155555555.0:53@s.whatsapp.net.
        webhook (Union[Unset, str]):  Example: https://some.site/webhook?request=parameter.
    """

    details: Union[Unset, str] = UNSET
    events: Union[Unset, str] = UNSET
    jid: Union[Unset, str] = UNSET
    webhook: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        events = self.events

        jid = self.jid

        webhook = self.webhook

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if events is not UNSET:
            field_dict["events"] = events
        if jid is not UNSET:
            field_dict["jid"] = jid
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        details = d.pop("details", UNSET)

        events = d.pop("events", UNSET)

        jid = d.pop("jid", UNSET)

        webhook = d.pop("webhook", UNSET)

        post_session_connect_response_200_data = cls(
            details=details,
            events=events,
            jid=jid,
            webhook=webhook,
        )

        post_session_connect_response_200_data.additional_properties = d
        return post_session_connect_response_200_data

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
