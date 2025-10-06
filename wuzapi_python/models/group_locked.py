from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GroupLocked")


@_attrs_define
class GroupLocked:
    """
    Attributes:
        group_jid (str): The JID of the group to configure Example: 120363312246943103@g.us.
        locked (bool): Whether to lock the group (true) or unlock it (false). When locked, only admins can modify group
            info. Example: True.
    """

    group_jid: str
    locked: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_jid = self.group_jid

        locked = self.locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "GroupJID": group_jid,
                "Locked": locked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_jid = d.pop("GroupJID")

        locked = d.pop("Locked")

        group_locked = cls(
            group_jid=group_jid,
            locked=locked,
        )

        group_locked.additional_properties = d
        return group_locked

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
