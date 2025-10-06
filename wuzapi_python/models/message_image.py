from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_image_context_info import MessageImageContextInfo


T = TypeVar("T", bound="MessageImage")


@_attrs_define
class MessageImage:
    """
    Attributes:
        phone (str):  Example: 5491155553935.
        image (str):  Example: data:image/jpeg;base64,iVBORw0.
        caption (Union[Unset, str]):  Example: Image Description.
        id (Union[Unset, str]):  Example: ABCDABCD1234.
        context_info (Union[Unset, MessageImageContextInfo]):
    """

    phone: str
    image: str
    caption: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    context_info: Union[Unset, "MessageImageContextInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        image = self.image

        caption = self.caption

        id = self.id

        context_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context_info, Unset):
            context_info = self.context_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Phone": phone,
                "Image": image,
            }
        )
        if caption is not UNSET:
            field_dict["Caption"] = caption
        if id is not UNSET:
            field_dict["Id"] = id
        if context_info is not UNSET:
            field_dict["ContextInfo"] = context_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_image_context_info import MessageImageContextInfo

        d = dict(src_dict)
        phone = d.pop("Phone")

        image = d.pop("Image")

        caption = d.pop("Caption", UNSET)

        id = d.pop("Id", UNSET)

        _context_info = d.pop("ContextInfo", UNSET)
        context_info: Union[Unset, MessageImageContextInfo]
        if isinstance(_context_info, Unset):
            context_info = UNSET
        else:
            context_info = MessageImageContextInfo.from_dict(_context_info)

        message_image = cls(
            phone=phone,
            image=image,
            caption=caption,
            id=id,
            context_info=context_info,
        )

        message_image.additional_properties = d
        return message_image

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
