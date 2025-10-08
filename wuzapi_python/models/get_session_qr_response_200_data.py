from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSessionQrResponse200Data")


@_attrs_define
class GetSessionQrResponse200Data:
    """
    Attributes:
        qrcode (Union[Unset, str]):  Example: data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQAAAAEAAQMAAABmvDolAAAABlBM
            VEX///8AAABVwtN+AAAEw0lEQVR42uyZPa7zqhaGX0ThLmsCkZlGCktMKaU76FxmSkgUmQZWJkA6CuT3avlLvrNvvRMX9x6KXWQ/UhCsn2cR/Lv+
            v5YhudQ6njEs1bBjqGYDwlJJpoOAArtUbK4Pi5jN3qPAlCkstcAeBazMUaoj78RpxGW4yWYzWVfmzwFLlLX4O+VkkucN5tFDOxiIAvfoA/X4uVQ4
            sgUcCBTYCG7AEGGKvbdrBabQ8OOyvg3ovm4ynqfLXJ9rvi+303ie5vm/gvZXgK6BLC7fo5hiG4KwW7b6I/2+DJi1+ybVFQyx6o6bbKPVDCyjTwcB
            ZB9uevBtAEafhiosCFH/4kNA8i1gg02B3KxezGbzEjUCDgIwYppR3SNdgtY3H0M1j8xFzCscvg/8uQvZAB9piidv1RXfZhbHdAwAlzsCNCaJDdMF
            4WQeeSGACZ8BMNl4FZYJA7j2YalPPhhngetHAaZPcyBg2wyYdAk0fKQ5yPja5PcBzTZW4uxJ2bTGwmxnu/BH4vwSgEsYItcCH+VZJt/AYhmHatbX
            dX8d2JvaTVzxCVW2aVhqheXSqvnR9b4L6AoUx3zX+jZd5rDB5jbLuv0txd8GRs+liuv+TsKloQWujxxRYf5s8gOA7fMVK9PQuDtMNCx2ibIdCMCy
            1s0yQU6Od9bqim1BuzoOAgzTHOiKv0d5Mt+XClN8DBxN/wxg2G2DbDYNJExCqE+Ne8poXoLxdUA/w5VrnxBQ9fjlqaJMwWgPAzLjtfKRW4A21ojn
            StX0dX2d5PeB0fawu2pChcuM4bk+tLmbMn0GMJslb5ptDXySbb5W1+0SyVcJOgRIQxSc7X0RUSvGs2DSeaz4gwCMNi/7XNACZc0KbPBtruv2KQA+
            DVFladBvt4xywhmh1Xd2fx8wzGTUltqCWrHWgqL7Jg8E0hSiFJfbUJ/Fpx3L1OHsVR8+APgoZMclUKvcft2+zTBrwjHArosim4ZcfW4Y4lVWnYXg
            2A8C9C5aEFXDoEJzmXFyfZoH/p0Wvw7oXoZbNQ823ase1wk2DQ3u7XK/BkzOqovwpM68Ko+jUyPFu6F8H4DvqsAuaUMZJ6+azjTPdS32KMBkLnpQ
            3VPnbsZgiktALW91/wDQEV5V7gT4JT6L62GRzeV0EDDC7rVFax2ZW6Aa6V5h/FEAgBlSbLrMVScU1s09+jxwG/9q87cB/Yxw3acBsk2Yw+nPf9Y1
            p88ARlNPtvPkF3LlPQYp8MtSx/FtpF8H4DNrZd8fOtTOxJSzXdo/c/fXAbN2DLeKs1dxHeEZZVWaju/3h18CcDk3qePZpllglDZ89MCq8nIQoDPA
            VaPi3iAFFwS1xjjr+HcYwD+hri216vBZzQbbZsE44RhAp+sQxfTpApGCoV1NOfsl4pX+nwC65a1uLnkK9TSuVTOhaQ4cBOzvtDcZXU5Bdl28SrF9
            HqrZJhwD7O/VsZpi7xSz7pXW6ahQ1/dB/RrYf2QhLBmr1lNINVRZfw9BBwArc4SszGlWWd2fxB9cFvJQYKnUUWAgV22y5v1e/ffHpiOAqMLCiOpy
            mwNGtxvk9s8mfwcU2CiydqvJbdKuSX0K8a/KHQDsMQkyeVbtISFif8mRcfwRtF8F/l3/O+s/AQAA///lM0dZSaTeTQAAAABJRU5ErkJggg==.
    """

    qrcode: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qrcode = self.qrcode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qrcode is not UNSET:
            field_dict["qrcode"] = qrcode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qrcode = d.pop("qrcode", UNSET)

        get_session_qr_response_200_data = cls(
            qrcode=qrcode,
        )

        get_session_qr_response_200_data.additional_properties = d
        return get_session_qr_response_200_data

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
