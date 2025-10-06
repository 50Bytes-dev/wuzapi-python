from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostChatSendEditResponse400")


@_attrs_define
class PostChatSendEditResponse400:
    """
    Attributes:
        code (Union[Unset, int]):  Example: 400.
        error (Union[Unset, str]):  Example: Invalid message ID or new content.
        success (Union[Unset, bool]):
    """

    code: Union[Unset, int] = UNSET
    error: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        error = self.error

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if error is not UNSET:
            field_dict["error"] = error
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        error = d.pop("error", UNSET)

        success = d.pop("success", UNSET)

        post_chat_send_edit_response_400 = cls(
            code=code,
            error=error,
            success=success,
        )

        post_chat_send_edit_response_400.additional_properties = d
        return post_chat_send_edit_response_400

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
