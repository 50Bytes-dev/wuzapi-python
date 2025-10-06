from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWebhookResponse200Data")


@_attrs_define
class GetWebhookResponse200Data:
    """
    Attributes:
        subscribe (Union[Unset, list[str]]):  Example: ['Message', 'ReadReceipt'].
        webhook (Union[Unset, str]):  Example: https://example.net/webhook.
    """

    subscribe: Union[Unset, list[str]] = UNSET
    webhook: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscribe: Union[Unset, list[str]] = UNSET
        if not isinstance(self.subscribe, Unset):
            subscribe = self.subscribe

        webhook = self.webhook

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscribe is not UNSET:
            field_dict["subscribe"] = subscribe
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscribe = cast(list[str], d.pop("subscribe", UNSET))

        webhook = d.pop("webhook", UNSET)

        get_webhook_response_200_data = cls(
            subscribe=subscribe,
            webhook=webhook,
        )

        get_webhook_response_200_data.additional_properties = d
        return get_webhook_response_200_data

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
