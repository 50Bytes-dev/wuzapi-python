from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_session_proxy_body import PostSessionProxyBody
from ...models.post_session_proxy_response_200 import PostSessionProxyResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostSessionProxyBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/session/proxy",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostSessionProxyResponse200]]:
    if response.status_code == 200:
        response_200 = PostSessionProxyResponse200.from_dict(response.json())

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
) -> Response[Union[Any, PostSessionProxyResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostSessionProxyBody,
) -> Response[Union[Any, PostSessionProxyResponse200]]:
    r"""Set Proxy Configuration

     Sets or disables the proxy configuration for the user.
    Provide a JSON payload with \"proxy_url\" (e.g. \"http://host:port\" or
    \"socks5://user:pass@host:port\") and \"enable\" (boolean).

    Args:
        body (PostSessionProxyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostSessionProxyResponse200]]
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
    body: PostSessionProxyBody,
) -> Optional[Union[Any, PostSessionProxyResponse200]]:
    r"""Set Proxy Configuration

     Sets or disables the proxy configuration for the user.
    Provide a JSON payload with \"proxy_url\" (e.g. \"http://host:port\" or
    \"socks5://user:pass@host:port\") and \"enable\" (boolean).

    Args:
        body (PostSessionProxyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostSessionProxyResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostSessionProxyBody,
) -> Response[Union[Any, PostSessionProxyResponse200]]:
    r"""Set Proxy Configuration

     Sets or disables the proxy configuration for the user.
    Provide a JSON payload with \"proxy_url\" (e.g. \"http://host:port\" or
    \"socks5://user:pass@host:port\") and \"enable\" (boolean).

    Args:
        body (PostSessionProxyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostSessionProxyResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostSessionProxyBody,
) -> Optional[Union[Any, PostSessionProxyResponse200]]:
    r"""Set Proxy Configuration

     Sets or disables the proxy configuration for the user.
    Provide a JSON payload with \"proxy_url\" (e.g. \"http://host:port\" or
    \"socks5://user:pass@host:port\") and \"enable\" (boolean).

    Args:
        body (PostSessionProxyBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostSessionProxyResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
