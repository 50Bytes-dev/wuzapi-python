from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_video_context_info import MessageVideoContextInfo


T = TypeVar("T", bound="MessageVideo")


@_attrs_define
class MessageVideo:
    """
    Attributes:
        phone (str):  Example: 5491155553935.
        video (str):  Example: data:video/mp4;base64,iVBORw0.
        caption (Union[Unset, str]):  Example: my video.
        id (Union[Unset, str]):  Example: ABCDABCD1234.
        jpeg_thumbnail (Union[Unset, str]):  Example: AA00D010.
        context_info (Union[Unset, MessageVideoContextInfo]):
    """

    phone: str
    video: str
    caption: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    jpeg_thumbnail: Union[Unset, str] = UNSET
    context_info: Union[Unset, "MessageVideoContextInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        video = self.video

        caption = self.caption

        id = self.id

        jpeg_thumbnail = self.jpeg_thumbnail

        context_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context_info, Unset):
            context_info = self.context_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Phone": phone,
                "Video": video,
            }
        )
        if caption is not UNSET:
            field_dict["Caption"] = caption
        if id is not UNSET:
            field_dict["Id"] = id
        if jpeg_thumbnail is not UNSET:
            field_dict["JpegThumbnail"] = jpeg_thumbnail
        if context_info is not UNSET:
            field_dict["ContextInfo"] = context_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_video_context_info import MessageVideoContextInfo

        d = dict(src_dict)
        phone = d.pop("Phone")

        video = d.pop("Video")

        caption = d.pop("Caption", UNSET)

        id = d.pop("Id", UNSET)

        jpeg_thumbnail = d.pop("JpegThumbnail", UNSET)

        _context_info = d.pop("ContextInfo", UNSET)
        context_info: Union[Unset, MessageVideoContextInfo]
        if isinstance(_context_info, Unset):
            context_info = UNSET
        else:
            context_info = MessageVideoContextInfo.from_dict(_context_info)

        message_video = cls(
            phone=phone,
            video=video,
            caption=caption,
            id=id,
            jpeg_thumbnail=jpeg_thumbnail,
            context_info=context_info,
        )

        message_video.additional_properties = d
        return message_video

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
