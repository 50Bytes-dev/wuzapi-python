from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_group_info_response_200 import GetGroupInfoResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    group_jid: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["groupJID"] = group_jid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/group/info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetGroupInfoResponse200]:
    if response.status_code == 200:
        response_200 = GetGroupInfoResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetGroupInfoResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    group_jid: str,
) -> Response[GetGroupInfoResponse200]:
    """Gets group information

     Retrieves information about a specific group

    Args:
        group_jid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupInfoResponse200]
    """

    kwargs = _get_kwargs(
        group_jid=group_jid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_jid: str,
) -> Optional[GetGroupInfoResponse200]:
    """Gets group information

     Retrieves information about a specific group

    Args:
        group_jid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupInfoResponse200
    """

    return sync_detailed(
        client=client,
        group_jid=group_jid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_jid: str,
) -> Response[GetGroupInfoResponse200]:
    """Gets group information

     Retrieves information about a specific group

    Args:
        group_jid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupInfoResponse200]
    """

    kwargs = _get_kwargs(
        group_jid=group_jid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_jid: str,
) -> Optional[GetGroupInfoResponse200]:
    """Gets group information

     Retrieves information about a specific group

    Args:
        group_jid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupInfoResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            group_jid=group_jid,
        )
    ).parsed
