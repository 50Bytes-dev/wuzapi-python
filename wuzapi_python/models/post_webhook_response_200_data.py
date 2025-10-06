from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostWebhookResponse200Data")


@_attrs_define
class PostWebhookResponse200Data:
    """
    Attributes:
        webhook_url (Union[Unset, str]):  Example: https://example.net/webhook.
        events (Union[Unset, list[str]]):  Example: ['Message', 'ReadReceipt'].
    """

    webhook_url: Union[Unset, str] = UNSET
    events: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_url = self.webhook_url

        events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_url is not UNSET:
            field_dict["WebhookURL"] = webhook_url
        if events is not UNSET:
            field_dict["Events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_url = d.pop("WebhookURL", UNSET)

        events = cast(list[str], d.pop("Events", UNSET))

        post_webhook_response_200_data = cls(
            webhook_url=webhook_url,
            events=events,
        )

        post_webhook_response_200_data.additional_properties = d
        return post_webhook_response_200_data

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
