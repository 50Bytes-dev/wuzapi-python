from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MessageButtonsContextInfo")


@_attrs_define
class MessageButtonsContextInfo:
    """
    Attributes:
        stanza_id (str):  Example: 3EB06F9067F80BAB89FF.
        participant (str):  Example: 5491155553935@s.whatsapp.net.
    """

    stanza_id: str
    participant: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stanza_id = self.stanza_id

        participant = self.participant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "StanzaId": stanza_id,
                "Participant": participant,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stanza_id = d.pop("StanzaId")

        participant = d.pop("Participant")

        message_buttons_context_info = cls(
            stanza_id=stanza_id,
            participant=participant,
        )

        message_buttons_context_info.additional_properties = d
        return message_buttons_context_info

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
