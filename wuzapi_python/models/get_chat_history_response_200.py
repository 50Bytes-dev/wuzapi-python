from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.history_message import HistoryMessage


T = TypeVar("T", bound="GetChatHistoryResponse200")


@_attrs_define
class GetChatHistoryResponse200:
    """
    Example:
        {'code': 200, 'success': True, 'data': [{'id': 1, 'user_id': 'abc123def456', 'chat_jid':
            '5491155553333@s.whatsapp.net', 'sender_jid': '5491155554444@s.whatsapp.net', 'message_id':
            '3EB0C767D26A1B5F7C83', 'timestamp': '2023-12-01T15:30:00Z', 'message_type': 'text', 'text_content': 'Hello, how
            are you?', 'media_link': ''}, {'id': 2, 'user_id': 'abc123def456', 'chat_jid': '5491155553333@s.whatsapp.net',
            'sender_jid': '5491155553333@s.whatsapp.net', 'message_id': '4FB1D878E37B2C6G8D94', 'timestamp':
            '2023-12-01T15:25:00Z', 'message_type': 'image', 'text_content': 'Check out this photo!', 'media_link':
            'https://example.com/media/image123.jpg'}]}

    Attributes:
        code (Union[Unset, int]):  Example: 200.
        success (Union[Unset, bool]):  Example: True.
        data (Union[Unset, list['HistoryMessage']]):
    """

    code: Union[Unset, int] = UNSET
    success: Union[Unset, bool] = UNSET
    data: Union[Unset, list["HistoryMessage"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        success = self.success

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if success is not UNSET:
            field_dict["success"] = success
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.history_message import HistoryMessage

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        success = d.pop("success", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = HistoryMessage.from_dict(data_item_data)

            data.append(data_item)

        get_chat_history_response_200 = cls(
            code=code,
            success=success,
            data=data,
        )

        get_chat_history_response_200.additional_properties = d
        return get_chat_history_response_200

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
