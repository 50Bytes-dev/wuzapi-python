from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_sticker_context_info import MessageStickerContextInfo


T = TypeVar("T", bound="MessageSticker")


@_attrs_define
class MessageSticker:
    """
    Attributes:
        phone (str):  Example: 5491155553935.
        sticker (str):  Example: data:image/webp;base64,iVBORw0.
        id (Union[Unset, str]):  Example: ABCDABCD1234.
        png_thumbnail (Union[Unset, str]):  Example: AA00D010.
        context_info (Union[Unset, MessageStickerContextInfo]):
    """

    phone: str
    sticker: str
    id: Union[Unset, str] = UNSET
    png_thumbnail: Union[Unset, str] = UNSET
    context_info: Union[Unset, "MessageStickerContextInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        sticker = self.sticker

        id = self.id

        png_thumbnail = self.png_thumbnail

        context_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context_info, Unset):
            context_info = self.context_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Phone": phone,
                "Sticker": sticker,
            }
        )
        if id is not UNSET:
            field_dict["Id"] = id
        if png_thumbnail is not UNSET:
            field_dict["PngThumbnail"] = png_thumbnail
        if context_info is not UNSET:
            field_dict["ContextInfo"] = context_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_sticker_context_info import MessageStickerContextInfo

        d = dict(src_dict)
        phone = d.pop("Phone")

        sticker = d.pop("Sticker")

        id = d.pop("Id", UNSET)

        png_thumbnail = d.pop("PngThumbnail", UNSET)

        _context_info = d.pop("ContextInfo", UNSET)
        context_info: Union[Unset, MessageStickerContextInfo]
        if isinstance(_context_info, Unset):
            context_info = UNSET
        else:
            context_info = MessageStickerContextInfo.from_dict(_context_info)

        message_sticker = cls(
            phone=phone,
            sticker=sticker,
            id=id,
            png_thumbnail=png_thumbnail,
            context_info=context_info,
        )

        message_sticker.additional_properties = d
        return message_sticker

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
