from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_ephemeral_duration import GroupEphemeralDuration

T = TypeVar("T", bound="GroupEphemeral")


@_attrs_define
class GroupEphemeral:
    """
    Attributes:
        group_jid (str): The JID of the group to configure ephemeral messages Example: 120363312246943103@g.us.
        duration (GroupEphemeralDuration): Duration for disappearing messages. Use "24h" for 24 hours, "7d" for 7 days,
            "90d" for 90 days, or "off" to disable. Example: 24h.
    """

    group_jid: str
    duration: GroupEphemeralDuration
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_jid = self.group_jid

        duration = self.duration.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "GroupJID": group_jid,
                "Duration": duration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_jid = d.pop("GroupJID")

        duration = GroupEphemeralDuration(d.pop("Duration"))

        group_ephemeral = cls(
            group_jid=group_jid,
            duration=duration,
        )

        group_ephemeral.additional_properties = d
        return group_ephemeral

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
