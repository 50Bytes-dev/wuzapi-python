from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_group_participants_action import UpdateGroupParticipantsAction

T = TypeVar("T", bound="UpdateGroupParticipants")


@_attrs_define
class UpdateGroupParticipants:
    """
    Attributes:
        group_jid (str): The JID of the group Example: 120363312246943103@g.us.
        action (UpdateGroupParticipantsAction): Action to perform ("add" to add participants, "remove" to remove
            participants, "promote" to promote participants, "demote" to demote participants.) Example: add.
        phone (list[str]):  Example: ['5491112345678', '5491123456789@s.whatsapp.net'].
    """

    group_jid: str
    action: UpdateGroupParticipantsAction
    phone: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_jid = self.group_jid

        action = self.action.value

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "GroupJID": group_jid,
                "Action": action,
                "Phone": phone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_jid = d.pop("GroupJID")

        action = UpdateGroupParticipantsAction(d.pop("Action"))

        phone = cast(list[str], d.pop("Phone"))

        update_group_participants = cls(
            group_jid=group_jid,
            action=action,
            phone=phone,
        )

        update_group_participants.additional_properties = d
        return update_group_participants

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
