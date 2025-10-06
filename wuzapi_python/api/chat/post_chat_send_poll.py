from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_poll import MessagePoll
from ...models.post_chat_send_poll_response_200 import PostChatSendPollResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: MessagePoll,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/send/poll",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostChatSendPollResponse200]:
    if response.status_code == 200:
        response_200 = PostChatSendPollResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostChatSendPollResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MessagePoll,
) -> Response[PostChatSendPollResponse200]:
    """Sends a Poll to some group

     Sends a Poll message. Group should contain the gid (group id), similar to 120363312246943103@g.us.

    Args:
        body (MessagePoll):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChatSendPollResponse200]
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
    body: MessagePoll,
) -> Optional[PostChatSendPollResponse200]:
    """Sends a Poll to some group

     Sends a Poll message. Group should contain the gid (group id), similar to 120363312246943103@g.us.

    Args:
        body (MessagePoll):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChatSendPollResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MessagePoll,
) -> Response[PostChatSendPollResponse200]:
    """Sends a Poll to some group

     Sends a Poll message. Group should contain the gid (group id), similar to 120363312246943103@g.us.

    Args:
        body (MessagePoll):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChatSendPollResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MessagePoll,
) -> Optional[PostChatSendPollResponse200]:
    """Sends a Poll to some group

     Sends a Poll message. Group should contain the gid (group id), similar to 120363312246943103@g.us.

    Args:
        body (MessagePoll):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChatSendPollResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
