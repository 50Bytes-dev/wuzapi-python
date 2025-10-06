from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_proxy_config import UserProxyConfig
    from ..models.user_s3_config import UserS3Config


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 4e4942c7dee1deef99ab8fd9f7350de5.
        name (Union[Unset, str]):  Example: John Doe.
        token (Union[Unset, str]):  Example: 1234ABCD.
        webhook (Union[Unset, str]):  Example: https://webhook.site/1234567890.
        events (Union[Unset, str]):  Example: All.
        proxy_config (Union[Unset, UserProxyConfig]):
        s3_config (Union[Unset, UserS3Config]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    webhook: Union[Unset, str] = UNSET
    events: Union[Unset, str] = UNSET
    proxy_config: Union[Unset, "UserProxyConfig"] = UNSET
    s3_config: Union[Unset, "UserS3Config"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        token = self.token

        webhook = self.webhook

        events = self.events

        proxy_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.proxy_config, Unset):
            proxy_config = self.proxy_config.to_dict()

        s3_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.s3_config, Unset):
            s3_config = self.s3_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if token is not UNSET:
            field_dict["token"] = token
        if webhook is not UNSET:
            field_dict["webhook"] = webhook
        if events is not UNSET:
            field_dict["events"] = events
        if proxy_config is not UNSET:
            field_dict["proxy_config"] = proxy_config
        if s3_config is not UNSET:
            field_dict["s3_config"] = s3_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_proxy_config import UserProxyConfig
        from ..models.user_s3_config import UserS3Config

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        token = d.pop("token", UNSET)

        webhook = d.pop("webhook", UNSET)

        events = d.pop("events", UNSET)

        _proxy_config = d.pop("proxy_config", UNSET)
        proxy_config: Union[Unset, UserProxyConfig]
        if isinstance(_proxy_config, Unset):
            proxy_config = UNSET
        else:
            proxy_config = UserProxyConfig.from_dict(_proxy_config)

        _s3_config = d.pop("s3_config", UNSET)
        s3_config: Union[Unset, UserS3Config]
        if isinstance(_s3_config, Unset):
            s3_config = UNSET
        else:
            s3_config = UserS3Config.from_dict(_s3_config)

        user = cls(
            id=id,
            name=name,
            token=token,
            webhook=webhook,
            events=events,
            proxy_config=proxy_config,
            s3_config=s3_config,
        )

        user.additional_properties = d
        return user

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
