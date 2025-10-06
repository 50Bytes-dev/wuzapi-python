from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_group_invitelink_response_200 import GetGroupInvitelinkResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    group_jid: str,
    reset: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["groupJID"] = group_jid

    params["reset"] = reset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/group/invitelink",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetGroupInvitelinkResponse200]:
    if response.status_code == 200:
        response_200 = GetGroupInvitelinkResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetGroupInvitelinkResponse200]:
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
    reset: Union[Unset, bool] = UNSET,
) -> Response[GetGroupInvitelinkResponse200]:
    """Get Group Invite Link

     Gets the invite link for a group, optionally resetting it to create a new/different one

    Args:
        group_jid (str):
        reset (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupInvitelinkResponse200]
    """

    kwargs = _get_kwargs(
        group_jid=group_jid,
        reset=reset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    group_jid: str,
    reset: Union[Unset, bool] = UNSET,
) -> Optional[GetGroupInvitelinkResponse200]:
    """Get Group Invite Link

     Gets the invite link for a group, optionally resetting it to create a new/different one

    Args:
        group_jid (str):
        reset (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupInvitelinkResponse200
    """

    return sync_detailed(
        client=client,
        group_jid=group_jid,
        reset=reset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    group_jid: str,
    reset: Union[Unset, bool] = UNSET,
) -> Response[GetGroupInvitelinkResponse200]:
    """Get Group Invite Link

     Gets the invite link for a group, optionally resetting it to create a new/different one

    Args:
        group_jid (str):
        reset (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupInvitelinkResponse200]
    """

    kwargs = _get_kwargs(
        group_jid=group_jid,
        reset=reset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    group_jid: str,
    reset: Union[Unset, bool] = UNSET,
) -> Optional[GetGroupInvitelinkResponse200]:
    """Get Group Invite Link

     Gets the invite link for a group, optionally resetting it to create a new/different one

    Args:
        group_jid (str):
        reset (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupInvitelinkResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            group_jid=group_jid,
            reset=reset,
        )
    ).parsed
