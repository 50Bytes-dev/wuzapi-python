from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReactionText")


@_attrs_define
class ReactionText:
    """
    Attributes:
        phone (str):  Example: 5491155553935.
        body (str):  Example: ❤️.
        id (str):  Example: me:3EB06F9067F80BAB89FF.
    """

    phone: str
    body: str
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        body = self.body

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Phone": phone,
                "Body": body,
                "Id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phone = d.pop("Phone")

        body = d.pop("Body")

        id = d.pop("Id")

        reaction_text = cls(
            phone=phone,
            body=body,
            id=id,
        )

        reaction_text.additional_properties = d
        return reaction_text

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
