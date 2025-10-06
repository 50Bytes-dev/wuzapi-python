from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_contact_context_info import MessageContactContextInfo


T = TypeVar("T", bound="MessageContact")


@_attrs_define
class MessageContact:
    """
    Attributes:
        phone (str):  Example: 5491155553935.
        name (str):  Example: John.
        vcard (str):  Example: BEGIN:VCARD
            VERSION:3.0
            N:Doe;John;;;
            FN:John Doe
            ORG:Example.com Inc.;
            TITLE:Imaginary test person
            EMAIL;type=INTERNET;type=WORK;type=pref:johnDoe@example.org
            TEL;type=WORK;type=pref:+1 617 555 1212
            TEL;type=WORK:+1 (617) 555-1234
            TEL;type=CELL:+1 781 555 1212
            TEL;type=HOME:+1 202 555 1212
            item1.ADR;type=WORK:;;2 Enterprise Avenue;Worktown;NY;01111;USA
            item1.X-ABADR:us
            item2.ADR;type=HOME;type=pref:;;3 Acacia Avenue;Hoitem2.X-ABADR:us
            END:VCARD.
        id (Union[Unset, str]):  Example: ABCDABCD1234.
        context_info (Union[Unset, MessageContactContextInfo]):
    """

    phone: str
    name: str
    vcard: str
    id: Union[Unset, str] = UNSET
    context_info: Union[Unset, "MessageContactContextInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        name = self.name

        vcard = self.vcard

        id = self.id

        context_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context_info, Unset):
            context_info = self.context_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Phone": phone,
                "Name": name,
                "Vcard": vcard,
            }
        )
        if id is not UNSET:
            field_dict["Id"] = id
        if context_info is not UNSET:
            field_dict["ContextInfo"] = context_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_contact_context_info import MessageContactContextInfo

        d = dict(src_dict)
        phone = d.pop("Phone")

        name = d.pop("Name")

        vcard = d.pop("Vcard")

        id = d.pop("Id", UNSET)

        _context_info = d.pop("ContextInfo", UNSET)
        context_info: Union[Unset, MessageContactContextInfo]
        if isinstance(_context_info, Unset):
            context_info = UNSET
        else:
            context_info = MessageContactContextInfo.from_dict(_context_info)

        message_contact = cls(
            phone=phone,
            name=name,
            vcard=vcard,
            id=id,
            context_info=context_info,
        )

        message_contact.additional_properties = d
        return message_contact

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
