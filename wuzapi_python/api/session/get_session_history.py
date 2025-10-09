from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_session_history_response_200 import GetSessionHistoryResponse200
from ...models.get_session_history_response_400 import GetSessionHistoryResponse400
from ...models.get_session_history_response_500 import GetSessionHistoryResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    chat_jid: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
    message_id: Union[Unset, str] = UNSET,
    timestamp: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["chat_jid"] = chat_jid

    params["limit"] = limit

    params["message_id"] = message_id

    params["timestamp"] = timestamp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/session/history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetSessionHistoryResponse200, GetSessionHistoryResponse400, GetSessionHistoryResponse500]]:
    if response.status_code == 200:
        response_200 = GetSessionHistoryResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSessionHistoryResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetSessionHistoryResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetSessionHistoryResponse200, GetSessionHistoryResponse400, GetSessionHistoryResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    chat_jid: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
    message_id: Union[Unset, str] = UNSET,
    timestamp: Union[Unset, str] = UNSET,
) -> Response[Union[GetSessionHistoryResponse200, GetSessionHistoryResponse400, GetSessionHistoryResponse500]]:
    """Request history sync

     Requests WhatsApp to sync message history for the connected session. Can sync all chats, a specific
    chat, or start from a specific message ID. Useful when history is disabled (history=0) and data is
    stored on external service.

    Args:
        chat_jid (Union[Unset, str]):  Example: 5491155553333@s.whatsapp.net.
        limit (Union[Unset, int]):  Default: 50. Example: 100.
        message_id (Union[Unset, str]):  Example: 3EB0C767D26A1B5F7C83.
        timestamp (Union[Unset, str]):  Example: 2023-12-01T15:30:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSessionHistoryResponse200, GetSessionHistoryResponse400, GetSessionHistoryResponse500]]
    """

    kwargs = _get_kwargs(
        chat_jid=chat_jid,
        limit=limit,
        message_id=message_id,
        timestamp=timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    chat_jid: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
    message_id: Union[Unset, str] = UNSET,
    timestamp: Union[Unset, str] = UNSET,
) -> Optional[Union[GetSessionHistoryResponse200, GetSessionHistoryResponse400, GetSessionHistoryResponse500]]:
    """Request history sync

     Requests WhatsApp to sync message history for the connected session. Can sync all chats, a specific
    chat, or start from a specific message ID. Useful when history is disabled (history=0) and data is
    stored on external service.

    Args:
        chat_jid (Union[Unset, str]):  Example: 5491155553333@s.whatsapp.net.
        limit (Union[Unset, int]):  Default: 50. Example: 100.
        message_id (Union[Unset, str]):  Example: 3EB0C767D26A1B5F7C83.
        timestamp (Union[Unset, str]):  Example: 2023-12-01T15:30:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSessionHistoryResponse200, GetSessionHistoryResponse400, GetSessionHistoryResponse500]
    """

    return sync_detailed(
        client=client,
        chat_jid=chat_jid,
        limit=limit,
        message_id=message_id,
        timestamp=timestamp,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    chat_jid: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
    message_id: Union[Unset, str] = UNSET,
    timestamp: Union[Unset, str] = UNSET,
) -> Response[Union[GetSessionHistoryResponse200, GetSessionHistoryResponse400, GetSessionHistoryResponse500]]:
    """Request history sync

     Requests WhatsApp to sync message history for the connected session. Can sync all chats, a specific
    chat, or start from a specific message ID. Useful when history is disabled (history=0) and data is
    stored on external service.

    Args:
        chat_jid (Union[Unset, str]):  Example: 5491155553333@s.whatsapp.net.
        limit (Union[Unset, int]):  Default: 50. Example: 100.
        message_id (Union[Unset, str]):  Example: 3EB0C767D26A1B5F7C83.
        timestamp (Union[Unset, str]):  Example: 2023-12-01T15:30:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetSessionHistoryResponse200, GetSessionHistoryResponse400, GetSessionHistoryResponse500]]
    """

    kwargs = _get_kwargs(
        chat_jid=chat_jid,
        limit=limit,
        message_id=message_id,
        timestamp=timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    chat_jid: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
    message_id: Union[Unset, str] = UNSET,
    timestamp: Union[Unset, str] = UNSET,
) -> Optional[Union[GetSessionHistoryResponse200, GetSessionHistoryResponse400, GetSessionHistoryResponse500]]:
    """Request history sync

     Requests WhatsApp to sync message history for the connected session. Can sync all chats, a specific
    chat, or start from a specific message ID. Useful when history is disabled (history=0) and data is
    stored on external service.

    Args:
        chat_jid (Union[Unset, str]):  Example: 5491155553333@s.whatsapp.net.
        limit (Union[Unset, int]):  Default: 50. Example: 100.
        message_id (Union[Unset, str]):  Example: 3EB0C767D26A1B5F7C83.
        timestamp (Union[Unset, str]):  Example: 2023-12-01T15:30:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetSessionHistoryResponse200, GetSessionHistoryResponse400, GetSessionHistoryResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
            chat_jid=chat_jid,
            limit=limit,
            message_id=message_id,
            timestamp=timestamp,
        )
    ).parsed
