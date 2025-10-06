from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_text import MessageText
from ...models.post_chat_send_text_response_200 import PostChatSendTextResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: MessageText,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/send/text",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostChatSendTextResponse200]:
    if response.status_code == 200:
        response_200 = PostChatSendTextResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostChatSendTextResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MessageText,
) -> Response[PostChatSendTextResponse200]:
    """Sends a text message

     Sends a text message. Phone and Body are mandatory. If no Id is supplied, a random one will be
    generated. ContextInfo is optional and used when repyling to some message. StanzaId is the message
    id we are replying to and participant who wrote that message. If sending a new message, ContextInfo
    can be ommited altogether.

    Args:
        body (MessageText):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChatSendTextResponse200]
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
    body: MessageText,
) -> Optional[PostChatSendTextResponse200]:
    """Sends a text message

     Sends a text message. Phone and Body are mandatory. If no Id is supplied, a random one will be
    generated. ContextInfo is optional and used when repyling to some message. StanzaId is the message
    id we are replying to and participant who wrote that message. If sending a new message, ContextInfo
    can be ommited altogether.

    Args:
        body (MessageText):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChatSendTextResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MessageText,
) -> Response[PostChatSendTextResponse200]:
    """Sends a text message

     Sends a text message. Phone and Body are mandatory. If no Id is supplied, a random one will be
    generated. ContextInfo is optional and used when repyling to some message. StanzaId is the message
    id we are replying to and participant who wrote that message. If sending a new message, ContextInfo
    can be ommited altogether.

    Args:
        body (MessageText):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChatSendTextResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MessageText,
) -> Optional[PostChatSendTextResponse200]:
    """Sends a text message

     Sends a text message. Phone and Body are mandatory. If no Id is supplied, a random one will be
    generated. ContextInfo is optional and used when repyling to some message. StanzaId is the message
    id we are replying to and participant who wrote that message. If sending a new message, ContextInfo
    can be ommited altogether.

    Args:
        body (MessageText):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChatSendTextResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
