from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_location_context_info import MessageLocationContextInfo


T = TypeVar("T", bound="MessageLocation")


@_attrs_define
class MessageLocation:
    """
    Attributes:
        phone (str):  Example: 5491155553935.
        latitude (float):  Example: 48.85837.
        longitude (float):  Example: 2.294481.
        name (Union[Unset, str]):  Example: Party.
        id (Union[Unset, str]):  Example: ABCDABCD1234.
        context_info (Union[Unset, MessageLocationContextInfo]):
    """

    phone: str
    latitude: float
    longitude: float
    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    context_info: Union[Unset, "MessageLocationContextInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        latitude = self.latitude

        longitude = self.longitude

        name = self.name

        id = self.id

        context_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context_info, Unset):
            context_info = self.context_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Phone": phone,
                "Latitude": latitude,
                "Longitude": longitude,
            }
        )
        if name is not UNSET:
            field_dict["Name"] = name
        if id is not UNSET:
            field_dict["Id"] = id
        if context_info is not UNSET:
            field_dict["ContextInfo"] = context_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_location_context_info import MessageLocationContextInfo

        d = dict(src_dict)
        phone = d.pop("Phone")

        latitude = d.pop("Latitude")

        longitude = d.pop("Longitude")

        name = d.pop("Name", UNSET)

        id = d.pop("Id", UNSET)

        _context_info = d.pop("ContextInfo", UNSET)
        context_info: Union[Unset, MessageLocationContextInfo]
        if isinstance(_context_info, Unset):
            context_info = UNSET
        else:
            context_info = MessageLocationContextInfo.from_dict(_context_info)

        message_location = cls(
            phone=phone,
            latitude=latitude,
            longitude=longitude,
            name=name,
            id=id,
            context_info=context_info,
        )

        message_location.additional_properties = d
        return message_location

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
