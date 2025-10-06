from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_user_proxy_config import CreateUserProxyConfig
    from ..models.create_user_s3_config import CreateUserS3Config


T = TypeVar("T", bound="CreateUser")


@_attrs_define
class CreateUser:
    """
    Attributes:
        name (str):  Example: John Doe.
        token (str):  Example: 1234ABCD.
        webhook (Union[Unset, str]): Webhook URL to receive events Example: https://webhook.site/1234567890.
        events (Union[Unset, str]): Events to subscribe to. Ex: 'All', 'Message', 'Presence' Example: All.
        proxy_config (Union[Unset, CreateUserProxyConfig]):
        s_3_config (Union[Unset, CreateUserS3Config]):
        history (Union[Unset, int]): Number of messages to store in history per chat for this user. 0 means no history
            is saved, any positive number enables history storage for that many messages per chat. Default is 0 Default: 0.
    """

    name: str
    token: str
    webhook: Union[Unset, str] = UNSET
    events: Union[Unset, str] = UNSET
    proxy_config: Union[Unset, "CreateUserProxyConfig"] = UNSET
    s_3_config: Union[Unset, "CreateUserS3Config"] = UNSET
    history: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        token = self.token

        webhook = self.webhook

        events = self.events

        proxy_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.proxy_config, Unset):
            proxy_config = self.proxy_config.to_dict()

        s_3_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.s_3_config, Unset):
            s_3_config = self.s_3_config.to_dict()

        history = self.history

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "token": token,
            }
        )
        if webhook is not UNSET:
            field_dict["webhook"] = webhook
        if events is not UNSET:
            field_dict["events"] = events
        if proxy_config is not UNSET:
            field_dict["proxyConfig"] = proxy_config
        if s_3_config is not UNSET:
            field_dict["s3Config"] = s_3_config
        if history is not UNSET:
            field_dict["history"] = history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_user_proxy_config import CreateUserProxyConfig
        from ..models.create_user_s3_config import CreateUserS3Config

        d = dict(src_dict)
        name = d.pop("name")

        token = d.pop("token")

        webhook = d.pop("webhook", UNSET)

        events = d.pop("events", UNSET)

        _proxy_config = d.pop("proxyConfig", UNSET)
        proxy_config: Union[Unset, CreateUserProxyConfig]
        if isinstance(_proxy_config, Unset):
            proxy_config = UNSET
        else:
            proxy_config = CreateUserProxyConfig.from_dict(_proxy_config)

        _s_3_config = d.pop("s3Config", UNSET)
        s_3_config: Union[Unset, CreateUserS3Config]
        if isinstance(_s_3_config, Unset):
            s_3_config = UNSET
        else:
            s_3_config = CreateUserS3Config.from_dict(_s_3_config)

        history = d.pop("history", UNSET)

        create_user = cls(
            name=name,
            token=token,
            webhook=webhook,
            events=events,
            proxy_config=proxy_config,
            s_3_config=s_3_config,
            history=history,
        )

        create_user.additional_properties = d
        return create_user

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
