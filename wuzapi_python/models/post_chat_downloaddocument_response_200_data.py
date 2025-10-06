from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostChatDownloaddocumentResponse200Data")


@_attrs_define
class PostChatDownloaddocumentResponse200Data:
    """
    Attributes:
        data (Union[Unset, str]):  Example: data:application/pdf;base64,iVBORw0KGgoA5CYII...=.
        mimetype (Union[Unset, str]):  Example: application/pdf.
    """

    data: Union[Unset, str] = UNSET
    mimetype: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        mimetype = self.mimetype

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["Data"] = data
        if mimetype is not UNSET:
            field_dict["Mimetype"] = mimetype

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("Data", UNSET)

        mimetype = d.pop("Mimetype", UNSET)

        post_chat_downloaddocument_response_200_data = cls(
            data=data,
            mimetype=mimetype,
        )

        post_chat_downloaddocument_response_200_data.additional_properties = d
        return post_chat_downloaddocument_response_200_data

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
