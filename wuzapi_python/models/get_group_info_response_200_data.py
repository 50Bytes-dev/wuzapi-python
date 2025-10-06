from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_group_info_response_200_data_participants_item import GetGroupInfoResponse200DataParticipantsItem


T = TypeVar("T", bound="GetGroupInfoResponse200Data")


@_attrs_define
class GetGroupInfoResponse200Data:
    """
    Attributes:
        announce_version_id (Union[Unset, str]):  Example: 1650572126123738.
        disappearing_timer (Union[Unset, int]):
        group_created (Union[Unset, str]):  Example: 2022-04-21T17:15:26-03:00.
        is_announce (Union[Unset, bool]):
        is_ephemeral (Union[Unset, bool]):
        is_locked (Union[Unset, bool]):
        jid (Union[Unset, str]):  Example: 120362023605733675@g.us.
        name (Union[Unset, str]):  Example: Super Group.
        name_set_at (Union[Unset, str]):  Example: 2022-04-21T17:15:26-03:00.
        name_set_by (Union[Unset, str]):  Example: 5491155554444@s.whatsapp.net.
        owner_jid (Union[Unset, str]):  Example: 5491155554444@s.whatsapp.net.
        participant_version_id (Union[Unset, str]):  Example: 1650234126145738.
        participants (Union[Unset, list['GetGroupInfoResponse200DataParticipantsItem']]):
        topic (Union[Unset, str]):
        topic_id (Union[Unset, str]):
        topic_set_at (Union[Unset, str]):  Example: 0001-01-01T00:00:00Z.
        topic_set_by (Union[Unset, str]):
    """

    announce_version_id: Union[Unset, str] = UNSET
    disappearing_timer: Union[Unset, int] = UNSET
    group_created: Union[Unset, str] = UNSET
    is_announce: Union[Unset, bool] = UNSET
    is_ephemeral: Union[Unset, bool] = UNSET
    is_locked: Union[Unset, bool] = UNSET
    jid: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    name_set_at: Union[Unset, str] = UNSET
    name_set_by: Union[Unset, str] = UNSET
    owner_jid: Union[Unset, str] = UNSET
    participant_version_id: Union[Unset, str] = UNSET
    participants: Union[Unset, list["GetGroupInfoResponse200DataParticipantsItem"]] = UNSET
    topic: Union[Unset, str] = UNSET
    topic_id: Union[Unset, str] = UNSET
    topic_set_at: Union[Unset, str] = UNSET
    topic_set_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        announce_version_id = self.announce_version_id

        disappearing_timer = self.disappearing_timer

        group_created = self.group_created

        is_announce = self.is_announce

        is_ephemeral = self.is_ephemeral

        is_locked = self.is_locked

        jid = self.jid

        name = self.name

        name_set_at = self.name_set_at

        name_set_by = self.name_set_by

        owner_jid = self.owner_jid

        participant_version_id = self.participant_version_id

        participants: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

        topic = self.topic

        topic_id = self.topic_id

        topic_set_at = self.topic_set_at

        topic_set_by = self.topic_set_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if announce_version_id is not UNSET:
            field_dict["AnnounceVersionID"] = announce_version_id
        if disappearing_timer is not UNSET:
            field_dict["DisappearingTimer"] = disappearing_timer
        if group_created is not UNSET:
            field_dict["GroupCreated"] = group_created
        if is_announce is not UNSET:
            field_dict["IsAnnounce"] = is_announce
        if is_ephemeral is not UNSET:
            field_dict["IsEphemeral"] = is_ephemeral
        if is_locked is not UNSET:
            field_dict["IsLocked"] = is_locked
        if jid is not UNSET:
            field_dict["JID"] = jid
        if name is not UNSET:
            field_dict["Name"] = name
        if name_set_at is not UNSET:
            field_dict["NameSetAt"] = name_set_at
        if name_set_by is not UNSET:
            field_dict["NameSetBy"] = name_set_by
        if owner_jid is not UNSET:
            field_dict["OwnerJID"] = owner_jid
        if participant_version_id is not UNSET:
            field_dict["ParticipantVersionID"] = participant_version_id
        if participants is not UNSET:
            field_dict["Participants"] = participants
        if topic is not UNSET:
            field_dict["Topic"] = topic
        if topic_id is not UNSET:
            field_dict["TopicID"] = topic_id
        if topic_set_at is not UNSET:
            field_dict["TopicSetAt"] = topic_set_at
        if topic_set_by is not UNSET:
            field_dict["TopicSetBy"] = topic_set_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_group_info_response_200_data_participants_item import (
            GetGroupInfoResponse200DataParticipantsItem,
        )

        d = dict(src_dict)
        announce_version_id = d.pop("AnnounceVersionID", UNSET)

        disappearing_timer = d.pop("DisappearingTimer", UNSET)

        group_created = d.pop("GroupCreated", UNSET)

        is_announce = d.pop("IsAnnounce", UNSET)

        is_ephemeral = d.pop("IsEphemeral", UNSET)

        is_locked = d.pop("IsLocked", UNSET)

        jid = d.pop("JID", UNSET)

        name = d.pop("Name", UNSET)

        name_set_at = d.pop("NameSetAt", UNSET)

        name_set_by = d.pop("NameSetBy", UNSET)

        owner_jid = d.pop("OwnerJID", UNSET)

        participant_version_id = d.pop("ParticipantVersionID", UNSET)

        participants = []
        _participants = d.pop("Participants", UNSET)
        for participants_item_data in _participants or []:
            participants_item = GetGroupInfoResponse200DataParticipantsItem.from_dict(participants_item_data)

            participants.append(participants_item)

        topic = d.pop("Topic", UNSET)

        topic_id = d.pop("TopicID", UNSET)

        topic_set_at = d.pop("TopicSetAt", UNSET)

        topic_set_by = d.pop("TopicSetBy", UNSET)

        get_group_info_response_200_data = cls(
            announce_version_id=announce_version_id,
            disappearing_timer=disappearing_timer,
            group_created=group_created,
            is_announce=is_announce,
            is_ephemeral=is_ephemeral,
            is_locked=is_locked,
            jid=jid,
            name=name,
            name_set_at=name_set_at,
            name_set_by=name_set_by,
            owner_jid=owner_jid,
            participant_version_id=participant_version_id,
            participants=participants,
            topic=topic,
            topic_id=topic_id,
            topic_set_at=topic_set_at,
            topic_set_by=topic_set_by,
        )

        get_group_info_response_200_data.additional_properties = d
        return get_group_info_response_200_data

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
