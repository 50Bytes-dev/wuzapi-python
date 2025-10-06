from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_chat_history_response_200 import GetChatHistoryResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    chat_jid: str,
    limit: Union[Unset, int] = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chat_jid"] = chat_jid

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chat/history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetChatHistoryResponse200]]:
    if response.status_code == 200:
        response_200 = GetChatHistoryResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = response.json()
        return response_400

    if response.status_code == 500:
        response_500 = response.json()
        return response_500

    if response.status_code == 501:
        response_501 = response.json()
        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetChatHistoryResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    chat_jid: str,
    limit: Union[Unset, int] = 50,
) -> Response[Union[Any, GetChatHistoryResponse200]]:
    """Get chat message history

     Retrieves message history for a specific chat. Returns messages in reverse chronological order
    (newest first). Requires message history to be enabled on the server.

    Args:
        chat_jid (str):  Example: 5491155553333@s.whatsapp.net.
        limit (Union[Unset, int]):  Default: 50. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetChatHistoryResponse200]]
    """

    kwargs = _get_kwargs(
        chat_jid=chat_jid,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    chat_jid: str,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[Any, GetChatHistoryResponse200]]:
    """Get chat message history

     Retrieves message history for a specific chat. Returns messages in reverse chronological order
    (newest first). Requires message history to be enabled on the server.

    Args:
        chat_jid (str):  Example: 5491155553333@s.whatsapp.net.
        limit (Union[Unset, int]):  Default: 50. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetChatHistoryResponse200]
    """

    return sync_detailed(
        client=client,
        chat_jid=chat_jid,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    chat_jid: str,
    limit: Union[Unset, int] = 50,
) -> Response[Union[Any, GetChatHistoryResponse200]]:
    """Get chat message history

     Retrieves message history for a specific chat. Returns messages in reverse chronological order
    (newest first). Requires message history to be enabled on the server.

    Args:
        chat_jid (str):  Example: 5491155553333@s.whatsapp.net.
        limit (Union[Unset, int]):  Default: 50. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetChatHistoryResponse200]]
    """

    kwargs = _get_kwargs(
        chat_jid=chat_jid,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    chat_jid: str,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[Any, GetChatHistoryResponse200]]:
    """Get chat message history

     Retrieves message history for a specific chat. Returns messages in reverse chronological order
    (newest first). Requires message history to be enabled on the server.

    Args:
        chat_jid (str):  Example: 5491155553333@s.whatsapp.net.
        limit (Union[Unset, int]):  Default: 50. Example: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetChatHistoryResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            chat_jid=chat_jid,
            limit=limit,
        )
    ).parsed
