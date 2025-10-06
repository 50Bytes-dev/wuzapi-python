from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_document_context_info import MessageDocumentContextInfo


T = TypeVar("T", bound="MessageDocument")


@_attrs_define
class MessageDocument:
    """
    Attributes:
        phone (str):  Example: 5491155553935.
        document (str):  Example: data:application/octet-stream;base64,aG9sYSBxdWUKdGFsCmNvbW8KZXN0YXMK.
        file_name (str):  Example: file.txt.
        id (Union[Unset, str]):  Example: ABCDABCD1234.
        context_info (Union[Unset, MessageDocumentContextInfo]):
    """

    phone: str
    document: str
    file_name: str
    id: Union[Unset, str] = UNSET
    context_info: Union[Unset, "MessageDocumentContextInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        document = self.document

        file_name = self.file_name

        id = self.id

        context_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context_info, Unset):
            context_info = self.context_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Phone": phone,
                "Document": document,
                "FileName": file_name,
            }
        )
        if id is not UNSET:
            field_dict["Id"] = id
        if context_info is not UNSET:
            field_dict["ContextInfo"] = context_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_document_context_info import MessageDocumentContextInfo

        d = dict(src_dict)
        phone = d.pop("Phone")

        document = d.pop("Document")

        file_name = d.pop("FileName")

        id = d.pop("Id", UNSET)

        _context_info = d.pop("ContextInfo", UNSET)
        context_info: Union[Unset, MessageDocumentContextInfo]
        if isinstance(_context_info, Unset):
            context_info = UNSET
        else:
            context_info = MessageDocumentContextInfo.from_dict(_context_info)

        message_document = cls(
            phone=phone,
            document=document,
            file_name=file_name,
            id=id,
            context_info=context_info,
        )

        message_document.additional_properties = d
        return message_document

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
