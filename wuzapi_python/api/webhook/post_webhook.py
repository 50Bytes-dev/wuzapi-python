from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_webhook_response_200 import PostWebhookResponse200
from ...models.webhook_set import WebhookSet
from ...types import Response


def _get_kwargs(
    *,
    body: WebhookSet,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhook",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostWebhookResponse200]:
    if response.status_code == 200:
        response_200 = PostWebhookResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostWebhookResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookSet,
) -> Response[PostWebhookResponse200]:
    """Sets webhook

     Sets the webhook that will be used to POST information when messages are received and configures the
    events to subscribe to.

    ## Webhook

    The following _webhook_ endpoints are used to get or set the webhook that will be called whenever a
    message or event is received. Available event types are:

    * Message
    * ReadReceipt
    * Presence
    * HistorySync
    * ChatPresence
    * All (subscribes to all event types)

    Args:
        body (WebhookSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostWebhookResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: WebhookSet,
) -> Optional[PostWebhookResponse200]:
    """Sets webhook

     Sets the webhook that will be used to POST information when messages are received and configures the
    events to subscribe to.

    ## Webhook

    The following _webhook_ endpoints are used to get or set the webhook that will be called whenever a
    message or event is received. Available event types are:

    * Message
    * ReadReceipt
    * Presence
    * HistorySync
    * ChatPresence
    * All (subscribes to all event types)

    Args:
        body (WebhookSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostWebhookResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookSet,
) -> Response[PostWebhookResponse200]:
    """Sets webhook

     Sets the webhook that will be used to POST information when messages are received and configures the
    events to subscribe to.

    ## Webhook

    The following _webhook_ endpoints are used to get or set the webhook that will be called whenever a
    message or event is received. Available event types are:

    * Message
    * ReadReceipt
    * Presence
    * HistorySync
    * ChatPresence
    * All (subscribes to all event types)

    Args:
        body (WebhookSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostWebhookResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: WebhookSet,
) -> Optional[PostWebhookResponse200]:
    """Sets webhook

     Sets the webhook that will be used to POST information when messages are received and configures the
    events to subscribe to.

    ## Webhook

    The following _webhook_ endpoints are used to get or set the webhook that will be called whenever a
    message or event is received. Available event types are:

    * Message
    * ReadReceipt
    * Presence
    * HistorySync
    * ChatPresence
    * All (subscribes to all event types)

    Args:
        body (WebhookSet):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostWebhookResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
