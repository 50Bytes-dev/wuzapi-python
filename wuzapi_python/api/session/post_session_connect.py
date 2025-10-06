from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connect import Connect
from ...types import Response


def _get_kwargs(
    *,
    body: Connect,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/session/connect",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Connect,
) -> Response[Any]:
    """connects to WhatsApp servers

     Initiates connection to WhatsApp servers.

    If there is no previous session created, it will generate a QR code that can be retrieved via the
    [qr](#/Session/get_session_qr) API call.

    If the optional Subscribe is supplied it will limit webhooks to the specified event types:
    Message,ReadReceipt,Presence,HistorySync,ChatPresence.

    If no Subscribe is supplied it will subscribe to All events.

    If Immediate is set to false, the action will wait for 10 seconds to retrieve actual connection
    status from whatsapp, otherwise it will return immediatly.

    When setting Immediate to true you should check for actual connection status after a few seconds via
    the [status](#/Session/get_session_status) API call as your connection might fail if the session was
    closed from another device.

    Args:
        body (Connect):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Connect,
) -> Response[Any]:
    """connects to WhatsApp servers

     Initiates connection to WhatsApp servers.

    If there is no previous session created, it will generate a QR code that can be retrieved via the
    [qr](#/Session/get_session_qr) API call.

    If the optional Subscribe is supplied it will limit webhooks to the specified event types:
    Message,ReadReceipt,Presence,HistorySync,ChatPresence.

    If no Subscribe is supplied it will subscribe to All events.

    If Immediate is set to false, the action will wait for 10 seconds to retrieve actual connection
    status from whatsapp, otherwise it will return immediatly.

    When setting Immediate to true you should check for actual connection status after a few seconds via
    the [status](#/Session/get_session_status) API call as your connection might fail if the session was
    closed from another device.

    Args:
        body (Connect):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
