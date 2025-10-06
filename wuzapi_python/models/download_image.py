from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DownloadImage")


@_attrs_define
class DownloadImage:
    """
    Attributes:
        url (str):
        media_key (str):
        mimetype (str):
        file_sha256 (str):
        file_length (float):
        direct_path (Union[Unset, str]):
        file_enc_sha256 (Union[Unset, str]):
    """

    url: str
    media_key: str
    mimetype: str
    file_sha256: str
    file_length: float
    direct_path: Union[Unset, str] = UNSET
    file_enc_sha256: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        media_key = self.media_key

        mimetype = self.mimetype

        file_sha256 = self.file_sha256

        file_length = self.file_length

        direct_path = self.direct_path

        file_enc_sha256 = self.file_enc_sha256

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Url": url,
                "MediaKey": media_key,
                "Mimetype": mimetype,
                "FileSHA256": file_sha256,
                "FileLength": file_length,
            }
        )
        if direct_path is not UNSET:
            field_dict["DirectPath"] = direct_path
        if file_enc_sha256 is not UNSET:
            field_dict["FileEncSHA256"] = file_enc_sha256

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("Url")

        media_key = d.pop("MediaKey")

        mimetype = d.pop("Mimetype")

        file_sha256 = d.pop("FileSHA256")

        file_length = d.pop("FileLength")

        direct_path = d.pop("DirectPath", UNSET)

        file_enc_sha256 = d.pop("FileEncSHA256", UNSET)

        download_image = cls(
            url=url,
            media_key=media_key,
            mimetype=mimetype,
            file_sha256=file_sha256,
            file_length=file_length,
            direct_path=direct_path,
            file_enc_sha256=file_enc_sha256,
        )

        download_image.additional_properties = d
        return download_image

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
