from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_audio_context_info import MessageAudioContextInfo


T = TypeVar("T", bound="MessageAudio")


@_attrs_define
class MessageAudio:
    """
    Attributes:
        phone (str):  Example: 5491155553935.
        audio (str):  Example: data:audio/ogg;base64,iVBORw0a.
        id (Union[Unset, str]):  Example: ABCDABCD1234.
        context_info (Union[Unset, MessageAudioContextInfo]):
    """

    phone: str
    audio: str
    id: Union[Unset, str] = UNSET
    context_info: Union[Unset, "MessageAudioContextInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        audio = self.audio

        id = self.id

        context_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context_info, Unset):
            context_info = self.context_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Phone": phone,
                "Audio": audio,
            }
        )
        if id is not UNSET:
            field_dict["Id"] = id
        if context_info is not UNSET:
            field_dict["ContextInfo"] = context_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_audio_context_info import MessageAudioContextInfo

        d = dict(src_dict)
        phone = d.pop("Phone")

        audio = d.pop("Audio")

        id = d.pop("Id", UNSET)

        _context_info = d.pop("ContextInfo", UNSET)
        context_info: Union[Unset, MessageAudioContextInfo]
        if isinstance(_context_info, Unset):
            context_info = UNSET
        else:
            context_info = MessageAudioContextInfo.from_dict(_context_info)

        message_audio = cls(
            phone=phone,
            audio=audio,
            id=id,
            context_info=context_info,
        )

        message_audio.additional_properties = d
        return message_audio

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
