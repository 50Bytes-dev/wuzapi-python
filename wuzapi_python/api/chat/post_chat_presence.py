from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_presence import ChatPresence
from ...models.post_chat_presence_response_200 import PostChatPresenceResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: ChatPresence,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/chat/presence",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostChatPresenceResponse200]:
    if response.status_code == 200:
        response_200 = PostChatPresenceResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostChatPresenceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ChatPresence,
) -> Response[PostChatPresenceResponse200]:
    r"""Sets chat presence

     Sends indication if you are writing or not (state could be either \"composing\" or \"paused\").
    Optional Media can be set to \"audio\" for indicating recording a message

    Args:
        body (ChatPresence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChatPresenceResponse200]
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
    body: ChatPresence,
) -> Optional[PostChatPresenceResponse200]:
    r"""Sets chat presence

     Sends indication if you are writing or not (state could be either \"composing\" or \"paused\").
    Optional Media can be set to \"audio\" for indicating recording a message

    Args:
        body (ChatPresence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChatPresenceResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ChatPresence,
) -> Response[PostChatPresenceResponse200]:
    r"""Sets chat presence

     Sends indication if you are writing or not (state could be either \"composing\" or \"paused\").
    Optional Media can be set to \"audio\" for indicating recording a message

    Args:
        body (ChatPresence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostChatPresenceResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ChatPresence,
) -> Optional[PostChatPresenceResponse200]:
    r"""Sets chat presence

     Sends indication if you are writing or not (state could be either \"composing\" or \"paused\").
    Optional Media can be set to \"audio\" for indicating recording a message

    Args:
        body (ChatPresence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostChatPresenceResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
