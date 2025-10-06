from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_webhook_response_200 import GetWebhookResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/webhook",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWebhookResponse200]:
    if response.status_code == 200:
        response_200 = GetWebhookResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWebhookResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetWebhookResponse200]:
    """Shows webhook

     Gets the configured webhook and subscribed events.

    ## Webhook

    The following _webhook_ endpoints are used to get or set the webhook that will be called whenever a
    message or event is received. Available event types are:

    * Message
    * ReadReceipt
    * Presence
    * HistorySync
    * ChatPresence
    * All (subscribes to all event types)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebhookResponse200]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[GetWebhookResponse200]:
    """Shows webhook

     Gets the configured webhook and subscribed events.

    ## Webhook

    The following _webhook_ endpoints are used to get or set the webhook that will be called whenever a
    message or event is received. Available event types are:

    * Message
    * ReadReceipt
    * Presence
    * HistorySync
    * ChatPresence
    * All (subscribes to all event types)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebhookResponse200
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[GetWebhookResponse200]:
    """Shows webhook

     Gets the configured webhook and subscribed events.

    ## Webhook

    The following _webhook_ endpoints are used to get or set the webhook that will be called whenever a
    message or event is received. Available event types are:

    * Message
    * ReadReceipt
    * Presence
    * HistorySync
    * ChatPresence
    * All (subscribes to all event types)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWebhookResponse200]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[GetWebhookResponse200]:
    """Shows webhook

     Gets the configured webhook and subscribed events.

    ## Webhook

    The following _webhook_ endpoints are used to get or set the webhook that will be called whenever a
    message or event is received. Available event types are:

    * Message
    * ReadReceipt
    * Presence
    * HistorySync
    * ChatPresence
    * All (subscribes to all event types)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWebhookResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
