from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_video import MessageVideo
from ...models.post_chat_send_video_response_200 import PostChatSendVideoResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: MessageVideo,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/send/video",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostChatSendVideoResponse200]:
    if response.status_code == 200:
        response_200 = PostChatSendVideoResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostChatSendVideoResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MessageVideo,
) -> Response[PostChatSendVideoResponse200]:
    """Sends a video message

     Sends a video message (must be base64 encoded in video/mp4 or video/3gpp format. Only H.264 video
    codec and AAC audio codec is supported.)

    Args:
        body (MessageVideo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChatSendVideoResponse200]
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
    body: MessageVideo,
) -> Optional[PostChatSendVideoResponse200]:
    """Sends a video message

     Sends a video message (must be base64 encoded in video/mp4 or video/3gpp format. Only H.264 video
    codec and AAC audio codec is supported.)

    Args:
        body (MessageVideo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChatSendVideoResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MessageVideo,
) -> Response[PostChatSendVideoResponse200]:
    """Sends a video message

     Sends a video message (must be base64 encoded in video/mp4 or video/3gpp format. Only H.264 video
    codec and AAC audio codec is supported.)

    Args:
        body (MessageVideo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChatSendVideoResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MessageVideo,
) -> Optional[PostChatSendVideoResponse200]:
    """Sends a video message

     Sends a video message (must be base64 encoded in video/mp4 or video/3gpp format. Only H.264 video
    codec and AAC audio codec is supported.)

    Args:
        body (MessageVideo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChatSendVideoResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
