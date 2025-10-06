from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_audio import MessageAudio
from ...models.post_chat_send_audio_response_200 import PostChatSendAudioResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: MessageAudio,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/send/audio",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostChatSendAudioResponse200]:
    if response.status_code == 200:
        response_200 = PostChatSendAudioResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostChatSendAudioResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MessageAudio,
) -> Response[PostChatSendAudioResponse200]:
    """Sends an audio message

     Sends an audio message (must be base64 encoded in opus format, mime type audio/ogg)

    Args:
        body (MessageAudio):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChatSendAudioResponse200]
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
    body: MessageAudio,
) -> Optional[PostChatSendAudioResponse200]:
    """Sends an audio message

     Sends an audio message (must be base64 encoded in opus format, mime type audio/ogg)

    Args:
        body (MessageAudio):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChatSendAudioResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MessageAudio,
) -> Response[PostChatSendAudioResponse200]:
    """Sends an audio message

     Sends an audio message (must be base64 encoded in opus format, mime type audio/ogg)

    Args:
        body (MessageAudio):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChatSendAudioResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MessageAudio,
) -> Optional[PostChatSendAudioResponse200]:
    """Sends an audio message

     Sends an audio message (must be base64 encoded in opus format, mime type audio/ogg)

    Args:
        body (MessageAudio):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChatSendAudioResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
