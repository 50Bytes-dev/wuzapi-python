from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_session_history_response_200 import GetSessionHistoryResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    count: Union[Unset, int] = UNSET,
    chat_jid: Union[Unset, str] = UNSET,
    oldest_msg_id: Union[Unset, str] = UNSET,
    oldest_msg_from_me: Union[Unset, bool] = UNSET,
    oldest_msg_timestamp: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["count"] = count

    params["chat_jid"] = chat_jid

    params["oldest_msg_id"] = oldest_msg_id

    params["oldest_msg_from_me"] = oldest_msg_from_me

    params["oldest_msg_timestamp"] = oldest_msg_timestamp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/session/history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetSessionHistoryResponse200]]:
    if response.status_code == 200:
        response_200 = GetSessionHistoryResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetSessionHistoryResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    count: Union[Unset, int] = UNSET,
    chat_jid: Union[Unset, str] = UNSET,
    oldest_msg_id: Union[Unset, str] = UNSET,
    oldest_msg_from_me: Union[Unset, bool] = UNSET,
    oldest_msg_timestamp: Union[Unset, int] = UNSET,
) -> Response[Union[Any, GetSessionHistoryResponse200]]:
    """Request history sync

     Requests WhatsApp to sync message history for the connected session. Supports query parameters to
    customize the sync request.

    Args:
        count (Union[Unset, int]):  Example: 50.
        chat_jid (Union[Unset, str]):  Example: 120363313346913103@g.us.
        oldest_msg_id (Union[Unset, str]):  Example: ABC123DEF456.
        oldest_msg_from_me (Union[Unset, bool]):  Example: True.
        oldest_msg_timestamp (Union[Unset, int]):  Example: 1640995200000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetSessionHistoryResponse200]]
    """

    kwargs = _get_kwargs(
        count=count,
        chat_jid=chat_jid,
        oldest_msg_id=oldest_msg_id,
        oldest_msg_from_me=oldest_msg_from_me,
        oldest_msg_timestamp=oldest_msg_timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    count: Union[Unset, int] = UNSET,
    chat_jid: Union[Unset, str] = UNSET,
    oldest_msg_id: Union[Unset, str] = UNSET,
    oldest_msg_from_me: Union[Unset, bool] = UNSET,
    oldest_msg_timestamp: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, GetSessionHistoryResponse200]]:
    """Request history sync

     Requests WhatsApp to sync message history for the connected session. Supports query parameters to
    customize the sync request.

    Args:
        count (Union[Unset, int]):  Example: 50.
        chat_jid (Union[Unset, str]):  Example: 120363313346913103@g.us.
        oldest_msg_id (Union[Unset, str]):  Example: ABC123DEF456.
        oldest_msg_from_me (Union[Unset, bool]):  Example: True.
        oldest_msg_timestamp (Union[Unset, int]):  Example: 1640995200000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetSessionHistoryResponse200]
    """

    return sync_detailed(
        client=client,
        count=count,
        chat_jid=chat_jid,
        oldest_msg_id=oldest_msg_id,
        oldest_msg_from_me=oldest_msg_from_me,
        oldest_msg_timestamp=oldest_msg_timestamp,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    count: Union[Unset, int] = UNSET,
    chat_jid: Union[Unset, str] = UNSET,
    oldest_msg_id: Union[Unset, str] = UNSET,
    oldest_msg_from_me: Union[Unset, bool] = UNSET,
    oldest_msg_timestamp: Union[Unset, int] = UNSET,
) -> Response[Union[Any, GetSessionHistoryResponse200]]:
    """Request history sync

     Requests WhatsApp to sync message history for the connected session. Supports query parameters to
    customize the sync request.

    Args:
        count (Union[Unset, int]):  Example: 50.
        chat_jid (Union[Unset, str]):  Example: 120363313346913103@g.us.
        oldest_msg_id (Union[Unset, str]):  Example: ABC123DEF456.
        oldest_msg_from_me (Union[Unset, bool]):  Example: True.
        oldest_msg_timestamp (Union[Unset, int]):  Example: 1640995200000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetSessionHistoryResponse200]]
    """

    kwargs = _get_kwargs(
        count=count,
        chat_jid=chat_jid,
        oldest_msg_id=oldest_msg_id,
        oldest_msg_from_me=oldest_msg_from_me,
        oldest_msg_timestamp=oldest_msg_timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    count: Union[Unset, int] = UNSET,
    chat_jid: Union[Unset, str] = UNSET,
    oldest_msg_id: Union[Unset, str] = UNSET,
    oldest_msg_from_me: Union[Unset, bool] = UNSET,
    oldest_msg_timestamp: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, GetSessionHistoryResponse200]]:
    """Request history sync

     Requests WhatsApp to sync message history for the connected session. Supports query parameters to
    customize the sync request.

    Args:
        count (Union[Unset, int]):  Example: 50.
        chat_jid (Union[Unset, str]):  Example: 120363313346913103@g.us.
        oldest_msg_id (Union[Unset, str]):  Example: ABC123DEF456.
        oldest_msg_from_me (Union[Unset, bool]):  Example: True.
        oldest_msg_timestamp (Union[Unset, int]):  Example: 1640995200000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetSessionHistoryResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            count=count,
            chat_jid=chat_jid,
            oldest_msg_id=oldest_msg_id,
            oldest_msg_from_me=oldest_msg_from_me,
            oldest_msg_timestamp=oldest_msg_timestamp,
        )
    ).parsed
